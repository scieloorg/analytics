# coding: utf-8
import logging
import sys
import json
from datetime import datetime, timedelta

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

cache_region = make_region(name='controller_cache')

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


def stats(*args, **kwargs):

    if not 'hosts' in kwargs:
        kwargs['hosts'] = ['esa.scielo.org', 'esb.scielo.org']

    st  = Stats(*args, **kwargs)

    return st

def articlemeta(host):

    address, port = host.split(':')

    return ArticleMeta(address, port)


def accessstats(host):

    address, port = host.split(':')

    return AccessStats(address, port)

def publicationstats(host):

    address, port = host.split(':')

    return PublicationStats(address, port)


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
    def general(self, index, field, code, collection, size=0):

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

        return self._compute_general(query_result, field)


class ArticleMeta(clients.ArticleMeta):

    @cache_region.cache_on_arguments()
    def certified_collections(self):
        try: 
            return self._certified_collections
        except AttributeError:
            self._certified_collections = {i.acronym:i.domain for i in self.collections() if i.status == 'certified'} 

        return self._certified_collections

    @cache_region.cache_on_arguments()
    def collections_journals(self, collection=None):

        if not collection:
            collections = self.certified_collections
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

        return self._journals[collection] if collection else self._journals
        

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
    def list_journals(self, code, collection, date_range_start=None, date_range_end=None):

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

        return self._compute_list_journals(query_result)

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
    def list_issues(self, code, collection, date_range_start=None, date_range_end=None):

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

        return self._compute_list_issues(query_result)

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
    def list_articles(self, code, collection, date_range_start=None, date_range_end=None):

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

        return self._compute_list_articles(query_result)


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
    def access_by_document_type(self, code, collection, date_range_start=None, date_range_end=None):

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

        return self._compute_access_by_document_type(query_result)


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
    def access_lifetime(self, code, collection, date_range_start=None, date_range_end=None):

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
                            "access_total": "desc"
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
                                    "access_total": "desc"
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
        
        return self._compute_access_lifetime(query_result)

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
    def access_by_month_and_year(self, code, collection, date_range_start=None, date_range_end=None):

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

        return self._compute_access_by_month_and_year(query_result)
