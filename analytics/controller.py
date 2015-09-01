# coding: utf-8
import logging
import sys
import json
from datetime import datetime

from thrift_clients import clients
from dogpile.cache import make_region
from xylose.scielodocument import Article, Journal

from analytics import utils

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
        
        if utils.REGEX_ISSN.match(code):
            return 'issn'

        if utils.REGEX_ISSUE.match(code):
            return 'issue'

        if utils.REGEX_ARTICLE.match(code):
            return 'pid'


    def access_by_document_type(self, code, collection):

        code_type = self._code_type(code)

        body = {
            "query": {
                "match_all": {}
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

        if code_type:
            body["query"] = {
                "match": {
                    code_type: code
                }
            }

        parameters = [
            clients.accessstats_thrift.kwargs('size', '0')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), parameters))

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

    def access_lifetime(sef, code, collection):
        body = {
            "query": {
                "match_all": {}
            },
            "size": 0,
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
                                "size": 4,
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

        charts = []

        parameters = [
            clients.accessstats_thrift.kwargs('size', '0')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), parameters))

        return query_result

    def access_by_month_and_year(self, code, collection):

        code_type = self._code_type(code)

        body = {
            "query": {
                "match_all": {}
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

        if code_type:
            body["query"] = {
                "match": {
                    code_type: code
                }
            }

        charts = []

        parameters = [
            clients.accessstats_thrift.kwargs('size', '0')
        ]

        query_result = json.loads(self.client.search(json.dumps(body), parameters))

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
