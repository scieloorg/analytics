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
from analytics.custom_queries import custom_query
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
    function_key_generator=utils.dogpile_controller_key_generator
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

    @staticmethod
    def _compute_received_self_and_granted_citation_chart(self_citations, granted_citations, received_citations):

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
        received_citations = self.bibliometrics.received_citations_by_year(issn, titles, raw=True)

        return self._compute_received_self_and_granted_citation_chart(self_citations, granted_citations, received_citations)

    @staticmethod
    def _compute_impact_factor(pub_citing_years, citable_docs):
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
                cit_docs[year]['fi_citations'].append(float(pcy.get(year, {}).get(str(i), 0)))
                cit_docs[year]['fi_documents'].append(float(cit_docs.get(str(i), {'citable_docs': 0})['citable_docs']))

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

        pub_citing_years = self.bibliometrics.publication_and_citing_years(issn, titles, citation_size=citation_size, raw=True)

        citable_docs = self.publication.citable_documents(issn, collection, raw=True)

        return self._compute_impact_factor(pub_citing_years, citable_docs)

    @staticmethod
    def _compute_impact_factor_chart(query_result):

        series = []
        for i in range(6):
            series.append({
                'name': 'impact_factor_%d' % i,
                'data': []
            })

        categories = []

        for base_year, data in sorted(query_result.items()):
            categories.append(base_year)
            for i in range(6):
                series[i]["data"].append(data['fi'][i])

        return {"series": series, "categories": categories}

    def impact_factor_chart(self, issn, collection, titles):

        query_result = self.impact_factor(issn, collection, titles, citation_size=0)

        return self._compute_impact_factor_chart(query_result)


class CitedbyStats(clients.Citedby):

    @staticmethod
    def _compute_publication_and_citing_years(query_result):
        """
        Metodo mantido apenas por padronização. Nenhum gráfico é montado
        diretamente com esses dados. Ele é utilizado em composição com outros
        resultados. POr esse motivo esta sendo retornado no formato padrão de
        resposta do ElasticSearch.
        """

        return query_result

    @cache_region.cache_on_arguments()
    def publication_and_citing_years(self, issn, titles, size=0, citation_size=0, raw=False):

        body = {
            "query": {
                "bool": {
                    "should": [],
                    "must_not": []
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

        for item in self._fuzzy_custom_query(issn, titles):
            body['query']['bool']['should'].append(item)

        for item in self._must_not_custom_query(issn):
            body['query']['bool']['must_not'].append(item)

        query_parameters = [
            clients.citedby_thrift.kwargs('size', '0'),
            clients.citedby_thrift.kwargs('search_type', 'count')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_publication_and_citing_years(query_result)

        return query_result if raw else computed

    @staticmethod
    def _compute_self_citations(query_result):

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
                "filtered": {
                    "query": {
                        "bool": {
                            "should": [],
                            "must_not": []
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

        for item in self._fuzzy_custom_query(issn, titles):
            body['query']['filtered']['query']['bool']['should'].append(item)

        for item in self._must_not_custom_query(issn):
            body['query']['filtered']['query']['bool']['must_not'].append(item)

        query_parameters = [
            clients.citedby_thrift.kwargs('size', '0'),
            clients.citedby_thrift.kwargs('search_type', 'count')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_self_citations(query_result)

        return query_result if raw else computed

    @staticmethod
    def _compute_granted_citations(query_result):

        items = []
        for bucket in query_result['aggregations']['reference_source']['buckets']:
            item = {
                "source": bucket['key'],
                "count": bucket['doc_count']
            }
            items.append(item)

        return items

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

    @staticmethod
    def _compute_received_citations_by_year(query_result):

        items = []
        for bucket in query_result['aggregations']['publication_year']['buckets']:
            item = {
                "source": bucket['key'],
                "count": bucket['doc_count']
            }
            items.append(item)

        return items

    @cache_region.cache_on_arguments()
    def received_citations_by_year(self, issn, titles, size=0, raw=False):

        body = {
            "query": {
                "bool": {
                    "should": [],
                    "must_not": []
                }
            },
            "aggs": {
                "publication_year": {
                    "terms": {
                        "field": "publication_year",
                        "size": size
                    }
                }
            }
        }

        for item in self._fuzzy_custom_query(issn, titles):
            body['query']['bool']['should'].append(item)

        for item in self._must_not_custom_query(issn):
            body['query']['bool']['must_not'].append(item)

        query_parameters = [
            clients.citedby_thrift.kwargs('size', '0'),
            clients.citedby_thrift.kwargs('search_type', 'count')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))
        # print json.dumps(body)
        computed = self._compute_received_citations_by_year(query_result)

        return query_result if raw else computed

    @staticmethod
    def _compute_received_citations(query_result):

        items = []
        for bucket in query_result['aggregations']['source']['buckets']:
            item = {
                "source": bucket['key'],
                "count": bucket['doc_count']
            }
            items.append(item)

        return items

    @cache_region.cache_on_arguments()
    def received_citations(self, issn, titles, size=0, raw=False):

        body = {
            "query": {
                "bool": {
                    "should": [],
                    "must_not": []
                }
            },
            "aggs": {
                "source": {
                    "terms": {
                        "field": "source",
                        "size": size
                    }
                }
            }
        }

        for item in self._fuzzy_custom_query(issn, titles):
            body['query']['bool']['should'].append(item)

        for item in self._must_not_custom_query(issn):
            body['query']['bool']['must_not'].append(item)

        query_parameters = [
            clients.citedby_thrift.kwargs('size', '0'),
            clients.citedby_thrift.kwargs('search_type', 'count')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_received_citations(query_result)

        return query_result if raw else computed

    @staticmethod
    def _compute_citing_forms(query_result):

        items = []
        for bucket in query_result['aggregations']['reference_source']['buckets']:
            item = {
                "source": bucket['key'],
                "count": bucket['doc_count']
            }
            items.append(item)

        return items

    @cache_region.cache_on_arguments()
    def citing_forms(self, issn, titles, size=0, raw=False):

        body = {
            "query": {
                "bool": {
                    "should": [],
                    "must_not": []
                }
            },
            "aggs": {
                "reference_source": {
                    "terms": {
                        "field": "reference_source",
                        "size": size
                    },
                }
            }
        }

        for item in self._fuzzy_custom_query(issn, titles):
            body['query']['bool']['should'].append(item)

        for item in self._must_not_custom_query(issn):
            body['query']['bool']['must_not'].append(item)

        query_parameters = [
            clients.citedby_thrift.kwargs('size', '0'),
            clients.citedby_thrift.kwargs('search_type', 'count')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_citing_forms(query_result)

        return query_result if raw else computed

    @staticmethod
    def _must_not_custom_query(issn):
        """
            Este metodo constroi a lista de filtros por título de periódico que
            será aplicada na pesquisa boleana como restrição "must_not".
            A lista de filtros é coletada do template de pesquisa customizada
            do periódico, quanto este template existir.
        """

        custom_queries = set([utils.clean_string(i) for i in custom_query.load(issn).get('must_not', [])])

        for item in custom_queries:

            query = {
                "match": {
                    "reference_source_cleaned": item
                }
            }

            yield query

    @staticmethod
    def _fuzzy_custom_query(issn, titles):
        """
            Este metodo constroi a lista de filtros por título de periódico que
            será aplicada na pesquisa boleana como match por similaridade "should".
            A lista de filtros é coletada do template de pesquisa customizada
            do periódico, quanto este template existir.
        """

        custom_queries = custom_query.load(issn).get('should', [])
        titles = [{'title': i} for i in titles if i not in [x['title'] for x in custom_queries]]
        titles.extend(custom_queries)

        for item in titles:

            if len(item['title'].strip()) == 0:
                continue

            query = {
                "fuzzy": {
                    "reference_source_cleaned": {
                        "value": utils.clean_string(item['title']),
                        "fuzziness": item.get('fuzziness', 3),
                        "max_expansions": 50
                    }
                }
            }

            yield query


class PublicationStats(clients.PublicationStats):

    @staticmethod
    def _code_type(code):

        if not code:
            return None

        if utils.REGEX_ISSN.match(code):
            return 'issn'

        if utils.REGEX_ISSUE.match(code):
            return 'issue'

        if utils.REGEX_ARTICLE.match(code):
            return 'pid'

    @staticmethod
    def _compute_granted_citations_by_year(query_result):
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
                    "must": [
                        {
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
            })

        query_parameters = [
            clients.publicationstats_thrift.kwargs('size', '0'),
        ]

        query_result = json.loads(self.client.search('article', json.dumps(body), query_parameters))

        computed = self._compute_granted_citations_by_year(query_result)

        return query_result if raw else computed

    @staticmethod
    def _compute_general(query_result, field):
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
            if field in ['publication_year', 'included_at_year']:
                documents['data'].append([utils.mktime(int(bucket['key'])), int(bucket['doc_count'])])
            else:
                documents['data'].append(int(bucket['doc_count']))

        series.append(documents)

        return {"series": series, "categories": categories}

    @cache_region.cache_on_arguments()
    def general(self, index, field, code, collection, size=0, sort_term=None, raw=False):

        sort_term = sort_term if sort_term in ['asc', 'desc'] else None

        body = {
            "query": {
                "bool": {
                    "must": [
                        {
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
            })

        query_parameters = [
            clients.publicationstats_thrift.kwargs('size', '0'),
            clients.publicationstats_thrift.kwargs('search_type', 'count')
        ]

        query_result = json.loads(self.client.search(index, json.dumps(body), query_parameters))

        computed = self._compute_general(query_result, field)

        return query_result if raw else computed

    @staticmethod
    def _compute_collection_size(query_result, field):

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

        if field not in ['issue', 'issn', 'citations', 'documents']:
            raise ValueError('Expected values for field: [issue, issn, citations, documents]')

        body = {
            "query": {
                "bool": {
                    "must": [
                        {
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
            })

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

    @staticmethod
    def _compute_citable_documents(query_result):

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

        navigator_series = []

        for bucket in query_result['aggregations']['publication_year']['buckets'][::-1]:
            amount = float(bucket['citable_documents']['doc_count']) + float(bucket['not_citable_documents']['doc_count'])
            year = utils.mktime(int(bucket['key']))
            navigator_series.append([year, amount])
            series[0]["data"].append({
                'x': year,
                'y': bucket['citable_documents']['doc_count'],
                'percentage': (bucket['citable_documents']['doc_count']/amount) * 100
            })
            series[1]["data"].append({
                'x': year,
                'y': bucket['not_citable_documents']['doc_count'],
                'percentage': (bucket['not_citable_documents']['doc_count']/amount) * 100
            })

        return {"series": series, "navigator_series": navigator_series}

    @cache_region.cache_on_arguments()
    def citable_documents(self, code, collection, raw=False):

        body = {
            "query": {
                "bool": {
                    "must": [
                        {
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
            })

        query_parameters = [
            clients.publicationstats_thrift.kwargs('size', '0'),
        ]

        query_result = json.loads(self.client.search('article', json.dumps(body), query_parameters))

        computed = self._compute_citable_documents(query_result)

        return query_result if raw else computed

    @cache_region.cache_on_arguments()
    def affiliations_by_publication_year(self, code, collection, raw=False):

        return self.by_publication_year(code, collection, 'aff_countries', raw)

    @cache_region.cache_on_arguments()
    def subject_areas_by_publication_year(self, code, collection, raw=False):

        return self.by_publication_year(code, collection, 'subject_areas', raw)

    @cache_region.cache_on_arguments()
    def languages_by_publication_year(self, code, collection, raw=False):

        return self.by_publication_year(code, collection, 'languages', raw)

    @cache_region.cache_on_arguments()
    def lincenses_by_publication_year(self, code, collection, raw=False):

        return self.by_publication_year(code, collection, 'license', raw)

    @staticmethod
    def _compute_by_publication_year(query_result, field):

        available_items = set()

        for year in query_result['aggregations']['publication_year']['buckets']:
            for bkt in year[field]['buckets']:
                available_items.add(bkt['key'])

        data = {}
        for year in query_result['aggregations']['publication_year']['buckets']:
            x = data.setdefault(year['key'], {k: 0 for k in available_items})
            for bkt in year[field]['buckets']:
                x[bkt['key']] = bkt['doc_count']

        series = []
        for item in sorted(available_items):
            series.append({
                'name': item,
                'data': []
            })

        navigator_series = []
        for year, bkts in sorted(data.items()):
            amount = float(sum([count for item, count in bkts.items()]))
            navigator_series.append([utils.mktime(int(year)), amount])
            for serie in series:
                serie["data"].append({
                    'x': utils.mktime(int(year)),
                    'y': bkts[serie['name']],
                    'percentage': (bkts[serie['name']]/amount) * 100
                })

        return {"series": series, "navigator_series": navigator_series}

    @cache_region.cache_on_arguments()
    def by_publication_year(self, code, collection, field, raw=False):

        allowed_fields = [
            'license', 'languages', 'subject_areas', 'aff_countries'
        ]

        field = field if field in allowed_fields else None

        body = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "collection": collection
                            }
                        }
                    ]
                }
            },
            "size": 0,
            "aggs": {
                "publication_year": {
                    "terms": {
                        "field": "publication_year",
                        "size": 0,
                        "order": {
                            "_term": "desc"
                        }
                    }

                }
            }
        }

        if field:
            body['aggs']['publication_year']['aggs'] = {
                field: {
                    "terms": {
                        "field": field,
                        "size": 0,
                    }
                }
            }

        code_type = self._code_type(code)

        if code_type:
            body["query"]["bool"]["must"].append({
                "match": {
                    code_type: code
                }
            })

        query_parameters = [
            clients.accessstats_thrift.kwargs('size', '0')
        ]

        # print json.dumps(body)
        query_result = json.loads(self.client.search('article', json.dumps(body), query_parameters))

        computed = self._compute_by_publication_year(query_result, field)

        return query_result if raw else computed


class ArticleMeta(clients.ArticleMeta):

    @cache_region.cache_on_arguments()
    def certified_collections(self):
        try:
            return self._certified_collections
        except AttributeError:
            self._certified_collections = {i.acronym: {'name': i.name, 'domain': i.domain} for i in self.collections() if i.has_analytics}

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

    @staticmethod
    def _code_type(code):

        if not code:
            return None

        if utils.REGEX_ISSN.match(code):
            return 'issn'

        if utils.REGEX_ISSUE.match(code):
            return 'issue'

        if utils.REGEX_ARTICLE.match(code):
            return 'pid'

    @staticmethod
    def _compute_list_journals(query_result):
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
            })

        query_parameters = [
            clients.accessstats_thrift.kwargs('size', '0')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_list_journals(query_result)

        return query_result if raw else computed

    @staticmethod
    def _compute_list_issues(query_result):
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
            })

        query_parameters = [
            clients.accessstats_thrift.kwargs('size', '0')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_list_issues(query_result)

        return query_result if raw else computed

    @staticmethod
    def _compute_list_articles(query_result):
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
            })

        query_parameters = [
            clients.accessstats_thrift.kwargs('size', '0')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_list_articles(query_result)

        return query_result if raw else computed

    @staticmethod
    def _compute_access_by_document_type(query_result):
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
            })

        query_parameters = [
            clients.accessstats_thrift.kwargs('size', '0')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_access_by_document_type(query_result)

        return query_result if raw else computed

    @staticmethod
    def _compute_access_lifetime(query_result):
        charts = []

        for bucket_access_year in query_result['aggregations']['access_year']['buckets']:
            access_total = {'name': bucket_access_year['key'], 'data': []}
            for bucket_access_total in bucket_access_year['publication_year']['buckets']:
                access_total['data'].append([utils.mktime(int(bucket_access_total['key'])), int(bucket_access_total['access_total']['value'])])

            charts.append({
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
            "size": 0,
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
                                "size": 0,
                                "order": {
                                    "_term": "asc"
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
            })

        query_parameters = [
            clients.accessstats_thrift.kwargs('size', '0')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_access_lifetime(query_result)

        return query_result if raw else computed

    @staticmethod
    def _compute_access_by_month_and_year(query_result):
        series = []
        navigator_series = []
        html = {'name': 'html', 'data': []}
        pdf = {'name': 'pdf', 'data': []}
        abstract = {'name': 'abstract', 'data': []}
        epdf = {'name': 'epdf', 'data': []}
        for bucket in query_result['aggregations']['access_date']['buckets']:
            amount = int(bucket['access_html']['value']) + int(bucket['access_pdf']['value']) + int(bucket['access_abstract']['value']) + int(bucket['access_epdf']['value'])
            navigator_series.append([bucket['key'], amount])
            html['data'].append([bucket['key'], int(bucket['access_html']['value'])])
            pdf['data'].append([bucket['key'], int(bucket['access_pdf']['value'])])
            abstract['data'].append([bucket['key'], int(bucket['access_abstract']['value'])])
            epdf['data'].append([bucket['key'], int(bucket['access_epdf']['value'])])

        series.append(html)
        series.append(pdf)
        series.append(abstract)
        series.append(epdf)

        return {'series': series, 'navigator_series': navigator_series}

    @cache_region.cache_on_arguments()
    def access_by_month_and_year(self, code, collection, date_range_start=None, date_range_end=None, raw=False):

        end = datetime.now()
        start = end - timedelta(365*3)

        date_range_start = date_range_start or start.isoformat()[0:10]
        date_range_end = date_range_end or end.isoformat()[0:10]

        body = {
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
            })

        query_parameters = [
            clients.accessstats_thrift.kwargs('size', '0')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), query_parameters))

        computed = self._compute_access_by_month_and_year(query_result)

        return query_result if raw else computed
