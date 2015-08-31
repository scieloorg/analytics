# coding: utf-8
import logging
import sys

import elasticsearch
from elasticsearch import ElasticsearchException
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient

from thrift_clients import clients
from dogpile.cache import make_region

from xylose.scielodocument import Article, Journal

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
        

class Stats(Elasticsearch):

    def _query_dispatcher(self, *args, **kwargs):

        try:
            data = self.search(*args, **kwargs)
        except elasticsearch.SerializationError as e:
            logging.exception(e)
            raise e
        except elasticsearch.TransportError as e:
            logging.exception(e)
            raise e
        except elasticsearch.ConnectionError as e:
            logging.exception(e)
            raise e
        except Exception as e:
            logging.exception(e)
            raise e

        return data

    def access_search(self, parameters):

        parameters['index'] = 'accesses'
        query_result = self._query_dispatcher(**parameters)

        return query_result

    def document(self, code, collection):

        body = {
            "query": {
                "bool": {
                    "must": [{
                            "match": {
                                "pid": code
                            }
                        },{
                            "match": {
                                "collection": collection
                            }

                        }

                    ]
                }
            },
            "aggs": {
                "access_total": {
                    "sum": {
                        "field": "access_total"
                    }
                },
                "access_html": {
                    "sum": {
                        "field": "access_html"
                    }
                },
                "access_pdf": {
                    "sum": {
                        "field": "access_pdf"
                    }
                },
                "access_abstract": {
                    "sum": {
                        "field": "access_abstract"
                    }
                },
                "access_epdf": {
                    "sum": {
                        "field": "access_epdf"
                    }
                }
            }
        }

        query_result = self._query_dispatcher(
            index='accesses',
            doc_type='articles',
            body=body,
            size=0
        )

        response = query_result['aggregations']

        return response

    def access_stats(self, doc_type, aggs, filters=None):

        if not aggs:
            raise ValueError(
                u'Aggregation not allowed, %s, expected %s' % (
                    str(aggs),
                    str(ALLOWED_DOC_TYPES_N_FACETS[doc_type])
                )
            )

        if not doc_type in ALLOWED_DOC_TYPES_N_FACETS.keys():
            raise ValueError(
                u'DocumentType not allowed, %s, expected %s' % (
                    doc_type,
                    str(ALLOWED_DOC_TYPES_N_FACETS.keys())
                )
            )
        
        for agg in aggs:
            if not agg in ALLOWED_DOC_TYPES_N_FACETS[doc_type]:
                raise ValueError(
                    u'Aggregation not allowed, %s, expected %s' % (
                        aggs,
                        str(ALLOWED_DOC_TYPES_N_FACETS[doc_type])
                    )
                )

        body = {
            "query": {
                "match_all": {}
            }
        }

        body.update(construct_aggs(aggs))

        if filters:
            must_terms = []
            for param, value in filters.items():
                if not param in ALLOWED_DOC_TYPES_N_FACETS[doc_type]:
                    raise ValueError(
                        u'Filter not allowed, %s expected %s' % (
                            param,
                            str(ALLOWED_DOC_TYPES_N_FACETS[doc_type])
                        )
                    )
                must_terms.append({'term': {param:value}})

            body['query'] = {
                "bool": {
                    "must": must_terms
                }
            }

        query_result = self._query_dispatcher(
            index='accesses',
            doc_type=doc_type,
            search_type='count',
            body=body
        )

        response = query_result['aggregations']

        return response

