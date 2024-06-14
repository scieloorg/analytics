# coding: utf-8
import json
import urllib.parse

from dogpile.cache import make_region
from scieloh5m5 import h5m5
# from scielojcr import jcrindicators
from articlemeta.client import ThriftClient as ArticleMetaThriftClient
from citedby.client import ThriftClient as CitedbyThriftClient
from publicationstats.client import ThriftClient as PublicationStatsThriftClient
from publicationstats import queries as PublicationStatsQueries
from citedby import custom_query
from altmetric import Altmetric, AltmetricHTTPException

from analytics import choices, utils, request_utils

PAGE_SIZE = 20


CITABLE_DOCUMENT_TYPES = (
    u'article-commentary',
    u'brief-report',
    u'case-report',
    u'data-article',
    u'rapid-communication',
    u'research-article',
    u'review-article'
)


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
                    "size": size
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


class Stats(object):

    def __init__(self, articlemeta_host, publicationstats_host, bibliometrics_host, usage_api_host):
        self.articlemeta = ArticleMeta()
        self.publication = PublicationStats()
        self.bibliometrics = BibliometricsStats()
        self.usage = UsageStats(usage_api_host)

    @property
    def _(self):
        return self.request.translate


class BibliometricsStats(CitedbyThriftClient):

    def _compute_google_h5m5(self, data):

        series = []
        categories = []

        series_h5 = {
            'name': 'H5',
            'data': []
        }

        series_m5 = {
            'name': 'M5',
            'data': []
        }

        for year, data in sorted(data.items()):
            categories.append(year)
            series_h5["data"].append(
                {'y': int(data['h5']), 'ownURL': data['url']})
            series_m5["data"].append(
                {'y': int(data['m5']), 'ownURL': data['url']})

        series.append(series_h5)
        series.append(series_m5)

        return {"series": series, "categories": categories}

    def google_h5m5(self, issn, raw=False):

        data = h5m5.get_metrics(issn) or {}

        if raw:
            return data

        return self._compute_google_h5m5(data)

    @cache_region.cache_on_arguments()
    def altmetric(self, issn):

        al = Altmetric()

        timeframes = ['1m', '3m', '6m', '1y', 'at']

        indicators = []

        for item in timeframes:

            try:
                value = al.journals(item, issns=issn)['results'][0]['stats']
                del(value['weeks_by_articles'])
            except KeyError as e:
                value = None
            except IndexError as e:
                value = None
            except TypeError as e:
                value = None
            except AltmetricHTTPException as e:
                value = None

            indicators.append((item, value))

        return indicators

    # def jcr(self, issn, raw=False):

    #     data = jcrindicators.get_indicators(issn) or {}

    #     return data

    # def _compute_jcr_impact_factor(self, data):

    #     series = []
    #     categories = []

    #     five_year_impact_factor = {
    #         'name': 'Fator de impacto 5 anos',
    #         'data': []
    #     }

    #     journal_impact_factor = {
    #         'name': 'Fator de impacto 2 anos',
    #         'data': []
    #     }

    #     impact_factor_without_journal_self_cites = {
    #         'name': 'Fator de impacto 2 anos, sem auto citação',
    #         'data': []
    #     }

    #     for year, data in sorted(data.items()):
    #         categories.append(year)
    #         five_year_impact_factor["data"].append(
    #             {'y': float(data['five_year_impact_factor']) if data['five_year_impact_factor'] else None}
    #         )
    #         journal_impact_factor["data"].append(
    #             {'y': float(data['journal_impact_factor']) if data['journal_impact_factor'] else None})
    #         impact_factor_without_journal_self_cites["data"].append(
    #             {'y': float(data['impact_factor_without_journal_self_cites']) if data['impact_factor_without_journal_self_cites'] else None})

    #     series.append(five_year_impact_factor)
    #     series.append(journal_impact_factor)
    #     series.append(impact_factor_without_journal_self_cites)

    #     return {"series": series, "categories": categories}

    # def jcr_impact_factor(self, issn):

    #     data = self.jcr(issn)

    #     return self._compute_jcr_impact_factor(data)

    # def _compute_jcr_average_impact_factor_percentile(self, data):

    #     series = []
    #     categories = []

    #     average_impact_factor_percentile = {
    #         'name': 'Fator de impacto (Média de percentil)',
    #         'data': []
    #     }

    #     for year, data in sorted(data.items()):
    #         categories.append(year)
    #         average_impact_factor_percentile["data"].append(
    #             {'y': float(data['average_journal_impact_factor_percentile']) if data['average_journal_impact_factor_percentile'] else None}
    #         )

    #     series.append(average_impact_factor_percentile)

    #     return {"series": series, "categories": categories}

    # def jcr_average_impact_factor_percentile(self, issn):

    #     data = self.jcr(issn)

    #     return self._compute_jcr_average_impact_factor_percentile(data)

    # def _compute_jcr_received_citations(self, data):

    #     series = []
    #     categories = []

    #     total_cites = {
    #         'name': 'Total de citações recebidas no ano',
    #         'data': []
    #     }

    #     for year, data in sorted(data.items()):
    #         categories.append(year)
    #         total_cites["data"].append(
    #             {'y': float(data['total_cites']) if data['total_cites'] else None}
    #         )

    #     series.append(total_cites)

    #     return {"series": series, "categories": categories}

    # def jcr_received_citations(self, issn):

    #     data = self.jcr(issn)

    #     return self._compute_jcr_received_citations(data)

    # def _compute_jcr_eigen_factor(self, data):

    #     series = []
    #     categories = []

    #     normalized_eigenfactor = {
    #         'name': 'Eigen Factor normalizado',
    #         'data': []
    #     }

    #     eigenfactor_score = {
    #         'name': 'Pontuação Eigen Factor',
    #         'data': []
    #     }

    #     for year, data in sorted(data.items()):
    #         categories.append(year)
    #         normalized_eigenfactor["data"].append(
    #             {'y': float(data['normalized_eigenfactor']) if data['normalized_eigenfactor'] else None}
    #         )
    #         eigenfactor_score["data"].append(
    #             {'y': float(data['eigenfactor_score']) if data['eigenfactor_score'] else None}
    #         )

    #     series.append(normalized_eigenfactor)
    #     series.append(eigenfactor_score)

    #     return {"series": series, "categories": categories}

    # def jcr_eigen_factor(self, issn):

    #     data = self.jcr(issn)

    #     return self._compute_jcr_eigen_factor(data)

    @staticmethod
    def _must_not_custom_query(issn):
        """
            Este metodo constroi a lista de filtros por título de periódico que
            será aplicada na pesquisa boleana como restrição "must_not".
            A lista de filtros é coletada do template de pesquisa customizada
            do periódico, quanto este template existir.
        """

        custom_queries = set([utils.clean_string(i) for i in custom_query.journal_titles.load(issn).get('must_not', [])])

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

        custom_queries = custom_query.journal_titles.load(issn).get('should', [])
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


class PublicationStats(PublicationStatsThriftClient):

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
    def list_subject_areas(self, code, collection):
        """
        Este método retorna uma lista de áreas temáticas disponíveis de acordo com os
        filtros indicados.

        Ex:
        [u'Health Sciences', u'Agricultural Sciences', u'Human Sciences']
        """

        result = self.general('article', 'subject_areas', code, collection, size=0, raw=True)

        subject_areas = [i['key'] for i in result['aggregations']['subject_areas']['buckets']]

        return subject_areas

    @cache_region.cache_on_arguments()
    def list_languages(self, code, collection):
        """
        Este método retorna uma lista de idiomas disponíveis de acordo com os
        filtros indicados.

        Ex:
        [u'PT', u'ES', u'EN']
        """

        result = self.general('article', 'languages', code, collection, size=0, raw=True)

        languages = [i['key'] for i in result['aggregations']['languages']['buckets']]

        return languages

    @cache_region.cache_on_arguments()
    def list_publication_years(self, code, collection):
        """
        Este método retorna uma lista de anos de publicação disponíveis de acordo
        com os filtros indicados.

        Ex:
        [u'2015', u'2016', u'2017']
        """

        result = self.general('article', 'publication_year', code, collection, size=0, raw=True)

        publication_year = sorted([i['key'] for i in result['aggregations']['publication_year']['buckets']])

        return publication_year

    @cache_region.cache_on_arguments()
    def general(self, index, field, code, collection, py_range=None, sa_scope=None, la_scope=None, size=0, sort_term=None, raw=False):

        sort_term = sort_term if sort_term in ['asc', 'desc'] else None

        body = {"query": {"filtered": {}}}

        fltr = {
            "filter": {
                "bool": {
                    "must": []
                }
            }
        }

        if py_range:
            fltr["filter"]["bool"]['must'].append(
                {
                    "range": {
                        "publication_year": {
                            "gte": py_range[0],
                            "lte": py_range[1]
                        }
                    }
                }
            )

        if sa_scope:
            fltr["filter"]["bool"]['must'].append(
                {
                    "terms": {
                        "subject_areas": sa_scope
                    }
                }
            )

        if la_scope:
            fltr["filter"]["bool"]['must'].append(
                {
                    "terms": {
                        "languages": la_scope
                    }
                }
            )

        query = {
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

        aggs = {
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
            aggs['aggs'][field]['terms']['order'] = {"_term": sort_term}

        code_type = self._code_type(code)

        if code_type:
            query["query"]["bool"]["must"].append({
                "match": {
                    code_type: code
                }
            })

        body['query']['filtered'].update(fltr)
        body['query']['filtered'].update(query)
        body.update(aggs)

        query_parameters = [
            ('size', '0'),
            ('search_type', 'count')
        ]

        query_result = self.search(index, json.dumps(body), query_parameters)

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
    def journals_status_detailde(self, collection):

        stats = PublicationStatsQueries.journals_status(collection)

        return stats

    @cache_region.cache_on_arguments()
    def collection_size(self, code, collection, field, py_range, sa_scope, la_scope, raw=False):

        if field not in ['issue', 'issn', 'citations', 'documents']:
            raise ValueError('Expected values for field: [issue, issn, citations, documents]')

        body = {"query": {"filtered": {}}}

        fltr = {
            "filter": {
                "bool": {
                    "must": [
                        {
                            "range": {
                                "publication_year": {
                                    "gte": py_range[0],
                                    "lte": py_range[1]
                                }
                            }
                        }, {
                            "terms": {
                                "subject_areas": sa_scope
                            }
                        }, {
                            "terms": {
                                "languages": la_scope
                            }
                        }
                    ]
                }
            }
        }

        query = {
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

        body['query']['filtered'].update(fltr)
        body['query']['filtered'].update(query)

        code_type = self._code_type(code)
        if code_type:
            query["query"]["bool"]["must"].append({
                "match": {
                    code_type: code
                }
            })

        query_parameters = [
            ('size', '0'),
            ('search_type', 'count')
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

        query_result = self.search('article', json.dumps(body), query_parameters)

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
    def citable_documents(self, code, collection, py_range=None, raw=False):

        body = {"query": {"filtered": {}}}

        if py_range:
            fltr = {
                "filter": {
                    "bool": {
                        "must": [
                            {
                                "range": {
                                    "publication_year": {
                                        "gte": py_range[0],
                                        "lte": py_range[1]
                                    }
                                }
                            }
                        ]
                    }
                }
            }
            body['query']['filtered'].update(fltr)

        query = {
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
        aggs = {
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
                                    "should": []
                                }
                            }
                        },
                        "not_citable_documents": {
                            "filter": {
                                "bool": {
                                    "must_not": []
                                }
                            }
                        }
                    }
                }
            }
        }

        for thematic_area in CITABLE_DOCUMENT_TYPES:
            aggs['aggs']['publication_year']['aggs']['citable_documents']['filter']['bool']['should'].append(
                {"term": {"document_type": thematic_area}}
            )

            aggs['aggs']['publication_year']['aggs']['not_citable_documents']['filter']['bool']['must_not'].append(
                {"term": {"document_type": thematic_area}}
            )

        code_type = self._code_type(code)

        if code_type:
            query["query"]["bool"]["must"].append({
                "match": {
                    code_type: code
                }
            })

        body['query']['filtered'].update(query)
        body.update(aggs)

        query_parameters = [
            ('size', '0'),
        ]

        query_result = self.search('article', json.dumps(body), query_parameters)

        computed = self._compute_citable_documents(query_result)

        return query_result if raw else computed

    @cache_region.cache_on_arguments()
    def affiliations_by_publication_year(self, code, collection, py_range, sa_scope, la_scope, raw=False):
        result = self.by_publication_year(code, collection, 'aff_countries', py_range, sa_scope,la_scope, raw)

        return result

    @cache_region.cache_on_arguments()
    def subject_areas_by_publication_year(self, code, collection, py_range, sa_scope, la_scope, raw=False):

        return self.by_publication_year(code, collection, 'subject_areas', py_range, sa_scope, la_scope, raw)

    @cache_region.cache_on_arguments()
    def document_type_by_publication_year(self, code, collection, py_range, sa_scope, la_scope, raw=False):

        return self.by_publication_year(code, collection, 'document_type', py_range, sa_scope, la_scope, raw)

    @cache_region.cache_on_arguments()
    def languages_by_publication_year(self, code, collection, py_range, sa_scope, la_scope, raw=False):

        result = self.by_publication_year(code, collection, 'languages', py_range, sa_scope, la_scope, raw)

        return result

    @cache_region.cache_on_arguments()
    def lincenses_by_publication_year(self, code, collection, py_range, sa_scope, la_scope, raw=False):

        return self.by_publication_year(code, collection, 'license', py_range, sa_scope, la_scope, raw)

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
    def by_publication_year(self, code, collection, field, py_range, sa_scope, la_scope, raw=False):

        body = {"query": {"filtered": {}}}

        fltr = {
            "filter": {
                "bool": {
                    "must": [
                        {
                            "range": {
                                "publication_year": {
                                    "gte": py_range[0],
                                    "lte": py_range[1]
                                }
                            }
                        }, {
                            "terms": {
                                "subject_areas": sa_scope
                            }
                        }, {
                            "terms": {
                                "languages": la_scope
                            }
                        }
                    ]
                }
            }
        }

        allowed_fields = [
            'license', 'languages', 'subject_areas', 'aff_countries', 'document_type'
        ]

        field = field if field in allowed_fields else None

        query = {
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

        aggs = {
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
            aggs['aggs']['publication_year']['aggs'] = {
                field: {
                    "terms": {
                        "field": field,
                        "size": 0,
                    }
                }
            }

        code_type = self._code_type(code)

        if code_type:
            query["query"]["bool"]["must"].append({
                "match": {
                    code_type: code
                }
            })

        body['query']['filtered'].update(fltr)
        body['query']['filtered'].update(query)
        body.update(aggs)

        query_parameters = [
            ('size', '0')
        ]

        query_result = self.search('article', json.dumps(body), query_parameters)

        computed = self._compute_by_publication_year(query_result, field)

        return query_result if raw else computed


class ArticleMeta(ArticleMetaThriftClient):

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


class UsageStats():
    def __init__(self, usage_api_base_url=None):
        self.base_url = usage_api_base_url or 'http://usage.apis.scielo.org/'
















    def _title_report_to_chart_data(self, json_results):
        serie_total_requests = []
        serie_unique_requests = []

        for i in json_results.get('Report_Items', [{},]):
            for p in i.get('Performance', {}):
                p_metric_label = p.get('Instance', {}).get('Metric_Type', '')
                p_metric_value = p.get('Instance', {}).get('Count', 0)
                p_period_begin = p.get('Period', {}).get('Begin_Date', '')

                fmt_date = self._format_date(p_period_begin)

                if p_metric_label  == 'Total_Item_Requests':
                    serie_total_requests.append([fmt_date, int(p_metric_value)])
                elif p_metric_label == 'Unique_Item_Requests':
                    serie_unique_requests.append([fmt_date, int(p_metric_value)])

        chart_data = {
            'series': [
                {'data': serie_total_requests, 'name': 'Total Item Requests',},
                {'data': serie_unique_requests, 'name': 'Unique Item Requests',}
            ],
        }

        return chart_data
    
    def _title_report_to_table_data(self, json_results):
        data = []

        for i in json_results.get('Report_Items', [{},]):
            if i.get('Title') or '' == '':
                continue

            i_article_language = i.get('Article_Language') or ''
            
            i_res = {
                'title': i['Title'],
                'article_language': choices.ISO_639_1.get(i_article_language.upper(), 'Undefined'),
                'unique_item_requests': 0, 
                'total_item_requests': 0
            }
            i_res.update({x['Type']: x['Value'] for x in i['Item_ID']})
            i_res['issn'] = i_res.get('Print_ISSN') or i_res.get('Online_ISSN') or ''
            
            for p in i.get('Performance', {}):
                p_metric_label = p.get('Instance', {}).get('Metric_Type', '')
                p_metric_value = p.get('Instance', {}).get('Count', 0)

                if p_metric_label == 'Unique_Item_Requests':
                    i_res['unique_item_requests'] += int(p_metric_value)
                elif p_metric_label  == 'Total_Item_Requests':
                    i_res['total_item_requests'] += int(p_metric_value)

            data.append(i_res)

        return sorted(data, key=lambda x: x.get('total_item_requests', 0), reverse=True)

    def get_usage_report(self, issn, collection, begin_date, end_date, granularity='monthly', report_code='tr_j1', api_version='v2', target='chart'):
        url_report = urllib.parse.urljoin(self.base_url, 'reports/%s' % report_code)

        params = {
            'issn': issn,
            'collection': collection,
            'begin_date': begin_date,
            'end_date': end_date,
            'granularity': granularity,
            'api': api_version,
        }

        self._clean_url_params(params, report_code)

        response = requests.get(
            url=url_report,
            params=params
        )

        try:
            response.raise_for_status()
        except requests.HTTPError:
            ...

        if response.status_code == 200:
            if report_code in ('cr_j1', 'tr_j1', 'lr_j1'):
                if target == 'chart':
                    return self._title_report_to_chart_data(response.json())
                elif target == 'table':
                    return self._title_report_to_table_data(response.json())
            
            if report_code in ('gr_j1',):
                if target == 'chart':
                    return self._geolocation_title_report_to_chart_data(response.json())

        return {}


    def _geolocation_title_report_to_chart_data(self, json_results):
        country_to_metrics = {}

        for i in json_results.get('Report_Items', {}):
            code = i['Access_Country_Code_']
            if code not in country_to_metrics:
                country_to_metrics[code] = {'Total_Item_Requests': 0}

            for p in i.get('Performance', {}):
                p_metric_label = p.get('Instance', {}).get('Metric_Type', '')

                if p_metric_label == 'Total_Item_Requests':
                    p_metric_value = p.get('Instance', {}).get('Count', 0)
                    country_to_metrics[code][p_metric_label] += int(p_metric_value)

        return [{'value': v['Total_Item_Requests'], 'code': k, 'name': k} for k, v in country_to_metrics.items() if v['Total_Item_Requests'] > 0]
    

    def _item_report_to_table_data(self, json_results):
        data = []

        for i in json_results.get('Report_Items', {}):
            i_res = {'code': '', 'total_item_requests': 0, 'unique_item_requests': 0}
            for p in i.get('Performance', {}):
                p_metric_label = p.get('Instance', {}).get('Metric_Type', '')
                p_metric_value = p.get('Instance', {}).get('Count', 0)

                if p_metric_label  == 'Total_Item_Requests':
                    i_res['total_item_requests'] += int(p_metric_value)
                elif p_metric_label == 'Unique_Item_Requests':
                    i_res['unique_item_requests'] += int(p_metric_value)

            if i_res['total_item_requests'] > 0:
                data.append(i_res)
        
        return data
