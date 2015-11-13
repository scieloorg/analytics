# coding: utf-8
import logging
import sys
import json
from datetime import datetime, timedelta

from pyramid.settings import aslist
from thrift_clients import clients
from dogpile.cache import make_region
from xylose.scielodocument import Article, Journal

from analytics import utils

PAGE_SIZE = 20

ALLOWED_DOC_TYPES_N_FACETS = {
    'articles': [
        'collection',
        'subject_areas',
        'languages',
        'aff_countries',
        'publication_year',
        'document_type',
        'issn',
        'pid',
        'access_date',
        'access_year'
    ]
}

cache_region = make_region(
    name='controller_cache',
    function_key_generator = utils.dogpile_controller_key_generator
)

def construct_aggs(aggs, size=0):
    """
    Construct the ElasticSearch aggretions query according to a list of
    parameters that must be aggregated.
    """

    data = {}
    point = None
    def join(field, point=None):
        default = {
            field: {
                "terms": {
                    "field": field,
                    "size": 0
                },
                "aggs": {
                    "access_total": {
                        "sum": {
                            "field": "access_total"
                        }
                    }
                }
            }
        }

        if point:
            point['aggs'].setdefault(field, default[field])
            return point['aggs'][field]
        else:
            data.setdefault('aggs', default)
            return data['aggs'][field]

    for item in aggs:
        point = join(item, point=point)

    return data


class ServerError(Exception):

    def __init__(self, value):
        self.message = 'Server Error: %s' % str(value)

    def __str__(self):
        return repr(self.message)


def articlemeta(host):

    address, port = host.split(':')

    return ArticleMeta(address, port)


def accessstats(host):

    address, port = host.split(':')

    return AccessStats(address, port)

def publicationstats(host):

    address, port = host.split(':')

    return PublicationStats(address, port)

def bibliometrics(host):

    address, port = host.split(':')

    return CitedbyStats(address, port)


class Stats(object):

    def __init__(self, articlemeta_host, publicationstats_host, accessstats_host, bibliometrics_host):
        self.articlemeta = articlemeta(articlemeta_host)
        self.publication = publicationstats(publicationstats_host)
        self.access = accessstats(accessstats_host)
        self.bibliometrics = bibliometrics(bibliometrics_host)

    def _compute_received_self_and_granted_citation_chart(self, self_citations, granted_citations, received_citations):

        joined_data = {}

        for item in self_citations['aggregations']['publication_year']['buckets']:
            joined_data.setdefault(item['key'], {'self_citation': 0, 'granted_citation': 0, 'received_citation': 0})
            joined_data[item['key']]['self_citation'] = item['doc_count']

        for item in granted_citations['aggregations']['publication_year']['buckets']:
            joined_data.setdefault(item['key'], {'self_citation': 0, 'granted_citation': 0, 'received_citation': 0})
            joined_data[item['key']]['granted_citation'] = item['citations']['value']
        

        for item in received_citations['aggregations']['publication_year']['buckets']:
            joined_data.setdefault(item['key'], {'self_citation': 0, 'granted_citation': 0, 'received_citation': 0})
            joined_data[item['key']]['received_citation'] = item['doc_count']


        data = {
            'series': [
                {
                    'name': 'granted_citation',
                    'data': []
                },
                {
                    'name': 'received_citation',
                    'data': []
                },
                {
                    'name': 'self_citation',
                    'data': []
                }
            ],
            'categories': []
        }

        for year, values in sorted(joined_data.items()):
            data['categories'].append(year)
            data['series'][0]['data'].append(values['granted_citation'])
            data['series'][1]['data'].append(values['received_citation'])
            data['series'][2]['data'].append(values['self_citation'])

        return data

    def received_self_and_granted_citation_chart(self, issn, collection, titles):

        self_citations = self.bibliometrics.self_citations(issn, titles, raw=True)
        granted_citations = self.publication.granted_citations_by_year(issn, collection, raw=True)
        received_citations = self.bibliometrics.received_citations_by_year(titles, raw=True)

        return self._compute_received_self_and_granted_citation_chart(self_citations, granted_citations, received_citations)

    def _compute_impact_factor(self, pub_citing_years, citable_docs):
        """
        Computa o fator de impacto em 2, 3 e 4 anos.
        """

        cit_docs = {}
        for pub_year in citable_docs['aggregations']['publication_year']['buckets']:
            cit_docs.setdefault(pub_year['key'], {'citable_docs': pub_year['citable_documents']['doc_count']})

        pcy = {}
        for publication_year in pub_citing_years['aggregations']['publication_year']['buckets']:
            pcy.setdefault(publication_year['key'], {})
            for citing_year in publication_year['reference_publication_year']['buckets']:
                pcy[publication_year['key']][citing_year['key']] = citing_year['doc_count']


        for year, content in cit_docs.items():
            cit_docs[year]['fi'] = []
            cit_docs[year]['fi_citations'] = []
            cit_docs[year]['fi_documents'] = []

            for i in range(int(year), int(year)-6, -1):
                cit_docs[year]['fi_citations'].append( float(pcy.get(year, {}).get(str(i), 0)) )
                cit_docs[year]['fi_documents'].append( float(cit_docs.get(str(i), {'citable_docs': 0})['citable_docs']) )

            for i in range(0, 6):
                first = 1 if i > 0 else 0
                last = i+1
                try:
                    cit_docs[year]['fi'].append(sum(cit_docs[year]['fi_citations'][first:last])/sum(cit_docs[year]['fi_documents'][first:last]))
                except:
                    cit_docs[year]['fi'].append(0)

        return cit_docs

    @cache_region.cache_on_arguments()
    def impact_factor(self, issn, collection, titles, citation_size=0):

        pub_citing_years = self.bibliometrics.publication_and_citing_years(titles, citation_size=citation_size, raw=True)

        citable_docs = self.publication.citable_documents(issn, collection, raw=True)

        return self._compute_impact_factor(pub_citing_years, citable_docs)

    def _compute_impact_factor_chart(self, query_result):

        series = []
        for i in range(6):
            series.append(
                {
                    'name': 'impact_factor_%d' % i,
                    'data': []
                }
            )

        categories = []

        for base_year, data in sorted(query_result.items()):
            categories.append(base_year)
            for i in range(6):
                series[i]["data"].append(data['fi'][i])

        return {"series": series, "categories": categories}

    def impact_factor_chart(self, issn, collection, titles):

        query_result = self.impact_factor(issn, collection, titles, citation_size=8)

        return self._compute_impact_factor_chart(query_result)

class CitedbyStats(clients.Citedby):

    def _compute_publication_and_citing_years(self, query_result):
        """
        Metodo mantido apenas por padronização. Nenhum gráfico é montado
        diretamente com esses dados. Ele é utilizado em composição com outros
        resultados. POr esse motivo esta sendo retornado no formato padrão de
        resposta do ElasticSearch.
        """

        return query_result

    @cache_region.cache_on_arguments()
    def publication_and_citing_years(self, titles, size=0, citation_size=0, raw=False):

        body = {
            "query": {
                "bool": {
                    "should": []
                }
            },
            "aggs": {
                "publication_year": {
                    "terms": {
                        "field": "publication_year",
                        "size": size
                    },
                    "aggs": {
                        "reference_publication_year": {
                            "terms": {
                                "field": "reference_publication_year",
                                "size": citation_size,
                                "order": {
                                    "_term": "desc"                                
                                }
                            }
                        }
                    }
                }
            }
        }

        for title in titles:

            if len(title.strip()) == 0:
                continue

            item = {
                "fuzzy": {
                    "reference_source_cleaned": {
                        "value": utils.clean_string(title),
                        "fuzziness" : 3,
                        "max_expansions": 50
                    }
                }
            }

            body['query']['bool']['should'].append(item)

        query_parameters = [
            clients.citedby_thrift.kwargs('size', '0'),
            clients.citedby_thrift.kwargs('search_type', 'count')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_publication_and_citing_years(query_result)

        return query_result if raw else computed

    def _compute_self_citations(self, query_result):

        series = [
            {
                'name': 'self_citations',
                'data': []
            }
        ]

        categories = []

        for bucket in query_result['aggregations']['publication_year']['buckets']:
            categories.append(bucket['key'])
            series[0]["data"].append(bucket['doc_count'])

        return {"series": series, "categories": categories}

    @cache_region.cache_on_arguments()
    def self_citations(self, issn, titles, size=0, raw=False):

        body = {
            "query": {
                "filtered" : {
                    "query": {
                        "bool": {
                            "should": []
                        }
                    },
                    "filter": {
                        "term": {
                            "issn": issn
                        }
                    }
                }
            },
            "aggs": {
                "publication_year": {
                    "terms": {
                        "field": "publication_year",
                        "size": size,
                        "order": {
                            "_term": "asc"
                        }
                    }
                }
            }
        }

        for title in titles:

            if len(title) == 0:
                continue

            item = {
                "fuzzy": {
                    "reference_source_cleaned": {
                        "value": utils.clean_string(title),
                        "fuzziness" : 3,
                        "max_expansions": 50
                    }
                }
            }

            body['query']['filtered']['query']['bool']['should'].append(item)

        query_parameters = [
            clients.citedby_thrift.kwargs('size', '0'),
            clients.citedby_thrift.kwargs('search_type', 'count')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_self_citations(query_result)

        return query_result if raw else computed


    def _compute_granted_citations(self, query_result):

        itens = []
        for bucket in query_result['aggregations']['reference_source']['buckets']:
            item = {
                "source": bucket['key'],
                "count": bucket['doc_count']
            }
            itens.append(item)

        return itens

    @cache_region.cache_on_arguments()
    def granted_citations(self, issn, size=0, raw=False):
        body = {
            "query": {
                "match": {
                    "issn": issn
                }
            },
            "aggs": {
                "reference_source": {
                    "terms": {
                        "field": "reference_source",
                        "size": size
                    }
                }
            }
        }

        query_parameters = [
            clients.citedby_thrift.kwargs('size', '0'),
            clients.citedby_thrift.kwargs('search_type', 'count')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_granted_citations(query_result)

        return query_result if raw else computed

    def _compute_received_citations_by_year(self, query_result):

        itens = []
        for bucket in query_result['aggregations']['publication_year']['buckets']:
            item = {
                "source": bucket['key'],
                "count": bucket['doc_count']
            }
            itens.append(item)

        return itens

    @cache_region.cache_on_arguments()
    def received_citations_by_year(self, titles, size=0, raw=False):

        body = {
            "query": {
                "bool": {
                    "should": []
                }
            },
            "aggs": {
                "publication_year": {
                    "terms": {
                        "field": "publication_year",
                        "size":size
                    }
                }
            }
        }

        for title in titles:

            if len(title.strip()) == 0:
                continue

            item = {
                "fuzzy": {
                    "reference_source_cleaned": {
                        "value": utils.clean_string(title),
                        "fuzziness" : 3,
                        "max_expansions": 50
                    }
                }
            }

            body['query']['bool']['should'].append(item)

        query_parameters = [
            clients.citedby_thrift.kwargs('size', '0'),
            clients.citedby_thrift.kwargs('search_type', 'count')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_received_citations_by_year(query_result)

        return query_result if raw else computed

    def _compute_received_citations(self, query_result):

        itens = []
        for bucket in query_result['aggregations']['source']['buckets']:
            item = {
                "source": bucket['key'],
                "count": bucket['doc_count']
            }
            itens.append(item)

        return itens

    @cache_region.cache_on_arguments()
    def received_citations(self, titles, size=0, raw=False):

        body = {
            "query": {
                "bool": {
                    "should": []
                }
            },
            "aggs": {
                "source": {
                    "terms": {
                        "field": "source",
                        "size":size
                    }
                }
            }
        }

        for title in titles:

            if len(title.strip()) == 0:
                continue

            item = {
                "fuzzy": {
                    "reference_source_cleaned": {
                        "value": utils.clean_string(title),
                        "fuzziness" : 3,
                        "max_expansions": 50
                    }
                }
            }

            body['query']['bool']['should'].append(item)

        query_parameters = [
            clients.citedby_thrift.kwargs('size', '0'),
            clients.citedby_thrift.kwargs('search_type', 'count')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_received_citations(query_result)

        return query_result if raw else computed


    def _compute_citing_forms(self, query_result):

        itens = []
        for bucket in query_result['aggregations']['reference_source']['buckets']:
            item = {
                "source": bucket['key'],
                "count": bucket['doc_count']
            }
            itens.append(item)

        return itens

    @cache_region.cache_on_arguments()
    def citing_forms(self, titles, size=0, raw=False):

        body = {
            "query": {
                "bool": {
                    "should": []
                }
            },
            "aggs": {
                "reference_source": {
                    "terms": {
                        "field": "reference_source",
                        "size":size
                    },
                }
            }
        }

        for title in titles:

            if len(title.strip()) == 0:
                continue

            item = {
                "fuzzy": {
                    "reference_source_cleaned": {
                        "value": utils.clean_string(title),
                        "fuzziness" : 3,
                        "max_expansions": 50
                    }
                }
            }

            body['query']['bool']['should'].append(item)

        query_parameters = [
            clients.citedby_thrift.kwargs('size', '0'),
            clients.citedby_thrift.kwargs('search_type', 'count')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_citing_forms(query_result)

        return query_result if raw else computed

class PublicationStats(clients.PublicationStats):

    def _code_type(self, code):

        if not code:
            return None
        
        if utils.REGEX_ISSN.match(code):
            return 'issn'

        if utils.REGEX_ISSUE.match(code):
            return 'issue'

        if utils.REGEX_ARTICLE.match(code):
            return 'pid'

    def _compute_granted_citations_by_year(self, query_result):
        series = [
            {
                'name': 'citations',
                'data': []
            }
        ]

        categories = []

        for bucket in query_result['aggregations']['publication_year']['buckets'][::-1]:
            categories.append(bucket['key'])
            series[0]["data"].append(bucket['citations']['value'])

        return {"series": series, "categories": categories}

    @cache_region.cache_on_arguments()
    def granted_citations_by_year(self, code, collection, raw=False):

        body = {
            "query": {
                "bool": {
                    "must": [{
                            "match": {
                                "collection": collection
                            }
                        }
                    ]
                }
            },
            "aggs": {
                "publication_year": {
                    "terms": {
                        "field": "publication_year",
                        "size": 0
                    },
                    "aggs": {
                        "citations": {
                            "sum": {
                                "field": "citations"
                            }
                        }
                    }
                }
            }
        }

        code_type = self._code_type(code)

        if code_type:
            body["query"]["bool"]["must"].append({
                    "match": {
                        code_type: code
                    }
                }
            )

        query_parameters = [
            clients.publicationstats_thrift.kwargs('size', '0'),
        ]

        query_result = json.loads(self.client.search('article', json.dumps(body), query_parameters))

        computed = self._compute_granted_citations_by_year(query_result)

        return query_result if raw else computed


    def _compute_general(self, query_result, field):
        series = [
            {
                "name": field,
                "data": []
            }
        ]

        for bucket in query_result['aggregations'][field]['buckets']:
            item = {
                "name": bucket['key'],
                "y": bucket['doc_count']
            }
            series[0]["data"].append(item)

        categories = []
        series = []
        documents = {'name': 'documents', 'data': []}
        for bucket in query_result['aggregations'][field]['buckets']:
            categories.append(bucket['key'])
            documents['data'].append(int(bucket['doc_count']))

        series.append(documents)


        return {"series": series, "categories": categories}

    @cache_region.cache_on_arguments()
    def general(self, index, field, code, collection, size=0, sort_term=None, raw=False):

        sort_term = sort_term if sort_term in ['asc', 'desc'] else None

        body = {
            "query": {
                "bool": {
                    "must": [{
                            "match": {
                                "collection": collection
                            }
                        }
                    ]
                }
            },
            "aggs": {
                field: {
                    "terms": {
                        "field": field,
                        "size": size
                    }
                }
            }
        }

        if sort_term:
            body['aggs'][field]['terms']['order'] = {"_term": sort_term}

        code_type = self._code_type(code)

        if code_type:
            body["query"]["bool"]["must"].append({
                    "match": {
                        code_type: code
                    }
                }
            )

        query_parameters = [
            clients.publicationstats_thrift.kwargs('size', '0'),
            clients.publicationstats_thrift.kwargs('search_type', 'count')
        ]

        query_result = json.loads(self.client.search(index, json.dumps(body), query_parameters))

        computed = self._compute_general(query_result, field)

        return query_result if raw else computed

    def _compute_collection_size(self, query_result, field):

        if field == 'documents':
            try:
                return {'total': query_result['hits']['total']}
            except:
                return None

        
        try:
            return {'total': query_result['aggregations'][field]['value']}
        except:
            return None

    @cache_region.cache_on_arguments()
    def collection_size(self, code, collection, field, raw=False):

        if not field in ['issue', 'issn', 'citations', 'documents']:
            raise ValueError('Expected values for field: [issue, issn, citations, documents]')

        body = {
            "query": {
                "bool": {
                    "must": [{
                            "match": {
                                "collection": collection
                            }
                        }
                    ]
                }
            }
        }

        code_type = self._code_type(code)

        if code_type:
            body["query"]["bool"]["must"].append({
                    "match": {
                        code_type: code
                    }
                }
            )

        query_parameters = [
            clients.publicationstats_thrift.kwargs('size', '0'),
            clients.publicationstats_thrift.kwargs('search_type', 'count')
        ]

        aggs_type = 'sum' if field == 'citations' else 'cardinality'

        if field != 'documents':
            body['aggs'] = { 
                field: {
                    aggs_type: {
                        "field": field
                    }
                }
            }

        query_result = json.loads(self.client.search('article', json.dumps(body), query_parameters))

        computed = self._compute_collection_size(query_result, field)

        return query_result if raw else computed

    def _compute_citable_documents(self, query_result):
        series = [
            {
                'name': 'citable_documents',
                'data': []
            },
            {
                'name': 'not_citable_documents',
                'data': []
            }
        ]

        categories = []

        for bucket in query_result['aggregations']['publication_year']['buckets'][::-1]:
            categories.append(bucket['key'])
            series[0]["data"].append(bucket['citable_documents']['doc_count'])
            series[1]["data"].append(bucket['not_citable_documents']['doc_count'])

        return {"series": series, "categories": categories}

    @cache_region.cache_on_arguments()
    def citable_documents(self, code, collection, raw=False):

        body = {
            "query": {
                "bool": {
                    "must": [{
                            "match": {
                                "collection": collection
                            }
                        }
                    ]
                }
            },
            "aggs": {
                "publication_year": {
                    "terms": {
                        "field": "publication_year",
                        "order": {
                            "_term": "desc"
                        },
                        "size": 0
                    },
                    "aggs": {
                        "citable_documents": {
                            "filter": {
                                "bool": {
                                    "should": [
                                        {
                                            "term": {
                                                "document_type": "research-article"
                                            }
                                        },
                                        {
                                            "term": {
                                                "document_type": "review-article"
                                            }
                                        }
                                    ]
                                }
                            }
                        },
                        "not_citable_documents": {
                            "filter": {
                                "bool": {
                                    "must_not": [
                                        {
                                            "term": {
                                                "document_type": "research-article"
                                            }
                                        },
                                        {
                                            "term": {
                                                "document_type": "review-article"
                                            }
                                        }
                                    ]
                                }
                            }
                        }
                    }
                }
            }
        }

        code_type = self._code_type(code)

        if code_type:
            body["query"]["bool"]["must"].append({
                    "match": {
                        code_type: code
                    }
                }
            )

        query_parameters = [
            clients.publicationstats_thrift.kwargs('size', '0'),
        ]

        query_result = json.loads(self.client.search('article', json.dumps(body), query_parameters))

        computed = self._compute_citable_documents(query_result)

        return query_result if raw else computed

class ArticleMeta(clients.ArticleMeta):

    @cache_region.cache_on_arguments()
    def certified_collections(self):
        try: 
            return self._certified_collections
        except AttributeError:
            self._certified_collections = {i.acronym:{'name': i.name, 'domain': i.domain} for i in self.collections() if i.has_analytics} 

        return self._certified_collections

    @cache_region.cache_on_arguments()
    def collections_journals(self, collection=None):

        if not collection:
            collections = self.certified_collections()
        else:
            collections = [collection]

        try: 
            return self._journals[collection] if collection else self._journals
        except AttributeError:
            self._journals = {}
            for collection in collections:
                for journal in self.journals(collection=collection):
                    coll = self._journals.setdefault(collection, {})
                    coll[journal.scielo_issn] = journal.title

        return self._journals.get(collection, {}) if collection else self._journals

class AccessStats(clients.AccessStats):

    def _code_type(self, code):

        if not code:
            return None
        
        if utils.REGEX_ISSN.match(code):
            return 'issn'

        if utils.REGEX_ISSUE.match(code):
            return 'issue'

        if utils.REGEX_ARTICLE.match(code):
            return 'pid'

    def _compute_list_journals(self, query_result):
        data = []

        for bucket in query_result['aggregations']['issn']['buckets']:
            item = {}
            item['issn'] = bucket['key']
            item['title'] = bucket['journal_title']['buckets'][0]['key']
            item['html'] = int(bucket['journal_title']['buckets'][0]['access_html']['value'])
            item['pdf'] = int(bucket['journal_title']['buckets'][0]['access_pdf']['value'])
            item['epdf'] = int(bucket['journal_title']['buckets'][0]['access_epdf']['value'])
            item['abstract'] = int(bucket['journal_title']['buckets'][0]['access_abstract']['value'])
            item['total'] = int(bucket['journal_title']['buckets'][0]['access_total']['value'])
            
            data.append(item)

        return data

    @cache_region.cache_on_arguments()
    def list_journals(self, code, collection, date_range_start=None, date_range_end=None, raw=False):

        end = datetime.now()
        start = end - timedelta(365*3)


        date_range_start = date_range_start or start.isoformat()
        date_range_end = date_range_end or end.isoformat()

        body = {
            "query": {
                "bool": {
                    "must": [{
                            "match": {
                                "collection": collection
                            }
                        },
                        {
                            "range": {
                                "access_date": {
                                    "gte": date_range_start,
                                    "lte": date_range_end
                                }
                            }
                        }
                    ]
                }
            },
            "size": 0,
            "aggs": {
                "issn": {
                    "terms": {
                        "field": "issn",
                        "size": 0,
                        "order": {
                            "1": "desc"
                        }
                  },
                  "aggs": {
                        "1": {
                            "sum": {
                                "field": "access_total"
                            }
                        },
                        "journal_title": {
                            "terms": {
                                "field": "journal_title",
                                "size": 0,
                                "order": {
                                    "access_total": "desc"
                                }
                            },
                            "aggs": {
                                "access_total": {
                                    "sum": {
                                        "field": "access_total"
                                    }
                                },
                                "access_epdf": {
                                    "sum": {
                                        "field": "access_epdf"
                                    }
                                },
                                "access_pdf": {
                                    "sum": {
                                        "field": "access_pdf"
                                    }
                                },
                                "access_html": {
                                    "sum": {
                                        "field": "access_html"
                                    }
                                },
                                "access_abstract": {
                                    "sum": {
                                        "field": "access_abstract"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        code_type = self._code_type(code)

        if code_type:
            body["query"]["bool"]["must"].append({
                    "match": {
                        code_type: code
                    }
                }
            )

        query_parameters = [
            clients.accessstats_thrift.kwargs('size', '0')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_list_journals(query_result)

        return query_result if raw else computed

    def _compute_list_issues(self, query_result):
        data = []

        for bucket in query_result['aggregations']['issue']['buckets']:
            item = {}
            item['issue'] = bucket['key']
            item['title'] = bucket['issue_title']['buckets'][0]['key']
            item['html'] = int(bucket['issue_title']['buckets'][0]['access_html']['value'])
            item['pdf'] = int(bucket['issue_title']['buckets'][0]['access_pdf']['value'])
            item['epdf'] = int(bucket['issue_title']['buckets'][0]['access_epdf']['value'])
            item['abstract'] = int(bucket['issue_title']['buckets'][0]['access_abstract']['value'])
            item['total'] = int(bucket['issue_title']['buckets'][0]['access_total']['value'])
            
            data.append(item)

        return data

    @cache_region.cache_on_arguments()
    def list_issues(self, code, collection, date_range_start=None, date_range_end=None, raw=False):

        end = datetime.now()
        start = end - timedelta(365*3)


        date_range_start = date_range_start or start.isoformat()
        date_range_end = date_range_end or end.isoformat()

        body = {
            "query": {
                "bool": {
                    "must": [{
                            "match": {
                                "collection": collection
                            }
                        },
                        {
                            "range": {
                                "access_date": {
                                    "gte": date_range_start,
                                    "lte": date_range_end
                                }
                            }
                        }
                    ]
                }
            },
            "size": 0,
            "aggs": {
                "issue": {
                    "terms": {
                        "field": "issue",
                        "size": 100,
                        "order": {
                            "1": "desc"
                        }
                  },
                  "aggs": {
                        "1": {
                            "sum": {
                                "field": "access_total"
                            }
                        },
                        "issue_title": {
                            "terms": {
                                "field": "issue_title",
                                "size": 1,
                                "order": {
                                    "access_total": "desc"
                                }
                            },
                            "aggs": {
                                "access_total": {
                                    "sum": {
                                        "field": "access_total"
                                    }
                                },
                                "access_epdf": {
                                    "sum": {
                                        "field": "access_epdf"
                                    }
                                },
                                "access_pdf": {
                                    "sum": {
                                        "field": "access_pdf"
                                    }
                                },
                                "access_html": {
                                    "sum": {
                                        "field": "access_html"
                                    }
                                },
                                "access_abstract": {
                                    "sum": {
                                        "field": "access_abstract"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        code_type = self._code_type(code)

        if code_type:
            body["query"]["bool"]["must"].append({
                    "match": {
                        code_type: code
                    }
                }
            )

        query_parameters = [
            clients.accessstats_thrift.kwargs('size', '0')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_list_issues(query_result)

        return query_result if raw else computed

    def _compute_list_articles(self, query_result):
        data = []

        for bucket in query_result['aggregations']['pid']['buckets']:
            item = {}
            item['pid'] = bucket['key']
            item['title'] = bucket['document_title']['buckets'][0]['key']
            item['html'] = int(bucket['document_title']['buckets'][0]['access_html']['value'])
            item['pdf'] = int(bucket['document_title']['buckets'][0]['access_pdf']['value'])
            item['epdf'] = int(bucket['document_title']['buckets'][0]['access_epdf']['value'])
            item['abstract'] = int(bucket['document_title']['buckets'][0]['access_abstract']['value'])
            item['total'] = int(bucket['document_title']['buckets'][0]['access_total']['value'])
            
            data.append(item)

        return data

    @cache_region.cache_on_arguments()
    def list_articles(self, code, collection, date_range_start=None, date_range_end=None, raw=False):

        end = datetime.now()
        start = end - timedelta(365*3)


        date_range_start = date_range_start or start.isoformat()
        date_range_end = date_range_end or end.isoformat()

        body = {
            "query": {
                "filtered": {
                    "query": {
                        "bool": {
                            "must": [
                                {
                                    "match": {
                                        "collection": collection
                                    }
                                },
                                {
                                    "range": {
                                        "access_date": {
                                            "gte": date_range_start,
                                            "lte": date_range_end
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    "filter": {
                        "exists": {
                            "field": "document_title"
                        }
                    }
                }
            },
            "size": 0,
            "aggs": {
                "pid": {
                    "terms": {
                        "field": "pid",
                        "size": 100,
                        "order": {
                            "1": "desc"
                        }
                  },
                  "aggs": {
                        "1": {
                            "sum": {
                                "field": "access_total"
                            }
                        },
                        "document_title": {
                            "terms": {
                                "field": "document_title",
                                "size": 1,
                                "order": {
                                    "access_total": "desc"
                                }
                            },
                            "aggs": {
                                "access_total": {
                                    "sum": {
                                        "field": "access_total"
                                    }
                                },
                                "access_epdf": {
                                    "sum": {
                                        "field": "access_epdf"
                                    }
                                },
                                "access_pdf": {
                                    "sum": {
                                        "field": "access_pdf"
                                    }
                                },
                                "access_html": {
                                    "sum": {
                                        "field": "access_html"
                                    }
                                },
                                "access_abstract": {
                                    "sum": {
                                        "field": "access_abstract"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        code_type = self._code_type(code)

        if code_type:
            body["query"]["filtered"]["query"]["bool"]["must"].append({
                    "match": {
                        code_type: code
                    }
                }
            )

        query_parameters = [
            clients.accessstats_thrift.kwargs('size', '0')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_list_articles(query_result)

        return query_result if raw else computed


    def _compute_access_by_document_type(self, query_result):
        series = [
            {
                "name": "Document Type",
                "data": []
            }
        ]

        for bucket in query_result['aggregations']['document_type']['buckets']:
            item = {
                "name": bucket['key'],
                "y": bucket['access_total']['value']
            }
            series[0]["data"].append(item)


        return {"series": series}

    @cache_region.cache_on_arguments()
    def access_by_document_type(self, code, collection, date_range_start=None, date_range_end=None, raw=False):

        end = datetime.now()
        start = end - timedelta(365*3)

        date_range_start = date_range_start or start.isoformat()[0:10]
        date_range_end = date_range_end or end.isoformat()[0:10]

        body = {
            "query": {
                "bool": {
                    "must": [{
                            "match": {
                                "collection": collection
                            }
                        },
                        {
                            "range": {
                                "access_date": {
                                    "gte": date_range_start,
                                    "lte": date_range_end
                                }
                            }
                        }
                    ]
                }
            },
            "size": 0,
            "aggs": {
                "document_type": {
                    "terms": {
                        "field": "document_type",
                        "size": 0
                    },
                    "aggs": {
                        "access_total": {
                            "sum": {
                                "field": "access_total"
                            }
                        }
                    }
                }
            }
        }

        code_type = self._code_type(code)

        if code_type:
            body["query"]["bool"]["must"].append({
                    "match": {
                        code_type: code
                    }
                }
            )

        query_parameters = [
            clients.accessstats_thrift.kwargs('size', '0')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_access_by_document_type(query_result)

        return query_result if raw else computed


    def _compute_access_lifetime(self, query_result):
        charts = []

        for bucket_access_year in query_result['aggregations']['access_year']['buckets']:
            access_total = {'name': bucket_access_year['key'], 'data': []}
            categories = []
            for bucket_access_total in bucket_access_year['publication_year']['buckets']:
                access_total['data'].append(int(bucket_access_total['access_total']['value']))
                categories.append(bucket_access_total['key'])
            
            charts.append({
                'categories': categories,
                'series': [access_total]
            })

        return charts

    @cache_region.cache_on_arguments()
    def access_lifetime(self, code, collection, date_range_start=None, date_range_end=None, raw=False):

        end = datetime.now()
        start = end - timedelta(365*3)

        date_range_start = date_range_start or start.isoformat()[0:10]
        date_range_end = date_range_end or end.isoformat()[0:10]

        body = {
            "query": {
                "bool": {
                    "must": [{
                            "match": {
                                "collection": collection
                            }
                        },
                        {
                            "range": {
                                "access_date": {
                                    "gte": date_range_start,
                                    "lte": date_range_end
                                }
                            }
                        }
                    ]
                }
            },            "size": 0,
            "aggs": {
                "access_year": {
                    "terms": {
                        "field": "access_year",
                        "size": 0,
                        "order": {
                            "_term": "desc"
                        }
                    },
                    "aggs": {
                        "access_total": {
                            "sum": {
                                "field": "access_total"
                            }
                        },
                        "publication_year": {
                            "terms": {
                                "field": "publication_year",
                                "size": 30,
                                "order": {
                                    "_term": "desc"
                                }
                            },
                            "aggs": {
                                "access_total": {
                                    "sum": {
                                        "field": "access_total"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        code_type = self._code_type(code)

        if code_type:
            body["query"]["bool"]["must"].append({
                    "match": {
                        code_type: code
                    }
                }
            )

        query_parameters = [
            clients.accessstats_thrift.kwargs('size', '0')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))
        
        computed = self._compute_access_lifetime(query_result)

        return query_result if raw else computed

    def _compute_access_by_month_and_year(self, query_result):
        categories = []
        series = []
        html = {'name': 'html', 'data': []}
        pdf = {'name': 'pdf', 'data': []}
        abstract = {'name': 'abstract', 'data': []}
        epdf = {'name': 'epdf', 'data': []}
        for bucket in query_result['aggregations']['access_date']['buckets']:
            categories.append(bucket['key_as_string'][0:7])
            html['data'].append(int(bucket['access_html']['value']))
            pdf['data'].append(int(bucket['access_pdf']['value']))
            abstract['data'].append(int(bucket['access_abstract']['value']))
            epdf['data'].append(int(bucket['access_epdf']['value']))

        series.append(html)
        series.append(pdf)
        series.append(abstract)
        series.append(epdf)

        return {'categories': categories, 'series': series}

    @cache_region.cache_on_arguments()
    def access_by_month_and_year(self, code, collection, date_range_start=None, date_range_end=None, raw=False):

        end = datetime.now()
        start = end - timedelta(365*3)

        date_range_start = date_range_start or start.isoformat()[0:10]
        date_range_end = date_range_end or end.isoformat()[0:10]

        body = {
            "query": {
                "bool": {
                    "must": [{
                            "match": {
                                "collection": collection
                            }
                        },
                        {
                            "range": {
                                "access_date": {
                                    "gte": date_range_start,
                                    "lte": date_range_end
                                }
                            }
                        }
                    ]
                }
            },
            "size": 0,
            "aggs": {
                "access_date": {
                    "terms": {
                        "field": "access_date",
                        "size": 0,
                        "order": {
                            "_term": "asc"
                        }
                    },
                    "aggs": {
                        "access_pdf": {
                            "sum": {
                                "field": "access_pdf"
                            }
                        },
                        "access_html": {
                            "sum": {
                                "field": "access_html"
                            }
                        },
                        "access_epdf": {
                            "sum": {
                                "field": "access_epdf"
                            }
                        },
                        "access_abstract": {
                            "sum": {
                                "field": "access_abstract"
                            }
                        }
                    }
                }
            }
        }

        code_type = self._code_type(code)

        if code_type:
            body["query"]["bool"]["must"].append({
                    "match": {
                        code_type: code
                    }
                }
            )

        query_parameters = [
            clients.accessstats_thrift.kwargs('size', '0')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_access_by_month_and_year(query_result)

        return query_result if raw else computed
