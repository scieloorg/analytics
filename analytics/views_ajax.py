# coding: utf-8
from pyramid.view import view_config

from dogpile.cache import make_region

from analytics.control_manager import base_data_manager
from analytics.custom_queries import custom_query

cache_region = make_region(name='views_ajax_cache')


@view_config(route_name='bibliometrics_journal_impact_factor_chart', request_method='GET', renderer='jsonp')
@base_data_manager
def bibliometrics_journal_impact_factor_chart(request):

    data = request.data_manager
    titles = request.GET.get('titles', None)

    titles = titles.split('||') if titles else []

    if data['selected_journal_code']:
        journal = request.stats.articlemeta.journal(code=data['selected_journal_code'])
        titles.append(journal.title)
        titles.append(journal.abbreviated_title)
        titles.extend(x['title'] for x in custom_query.load(data['selected_journal_code']).get('should', []) if x['title'] not in titles)

    data = request.stats.impact_factor_chart(data['selected_journal_code'], data['selected_collection_code'], titles, py_range=data['py_range'])

    return request.chartsconfig.bibliometrics_impact_factor(data)


@view_config(route_name='bibliometrics_journal_received_self_and_granted_citation_chart', request_method='GET', renderer='jsonp')
@base_data_manager
def bibliometrics_journal_received_self_and_granted_citation_chart(request):

    data = request.data_manager
    titles = request.GET.get('titles', None)

    titles = titles.split('||') if titles else []

    if data['selected_journal_code']:
        journal = request.stats.articlemeta.journal(code=data['selected_journal_code'])
        titles.append(journal.title)
        titles.append(journal.abbreviated_title)
        titles.extend(x['title'] for x in custom_query.load(data['selected_journal_code']).get('should', []) if x['title'] not in titles)

    data = request.stats.received_self_and_granted_citation_chart(data['selected_journal_code'], data['selected_collection_code'], titles, py_range=data['py_range'])

    return request.chartsconfig.bibliometrics_journal_received_self_and_granted_citation_chart(data)


@view_config(route_name='publication_article_references', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_article_references(request):

    data = request.data_manager

    chart_data = request.stats.publication.general('article', 'citations', data['selected_code'], data['selected_collection_code'], py_range=data['py_range'], sa_scope=data['sa_scope'], la_scope=data['la_scope'], size=40, sort_term='asc')

    return request.chartsconfig.publication_article_references(chart_data)


@view_config(route_name='publication_article_authors', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_article_authors(request):

    data = request.data_manager

    chart_data = request.stats.publication.general('article', 'authors', data['selected_code'], data['selected_collection_code'], py_range=data['py_range'], sa_scope=data['sa_scope'], la_scope=data['la_scope'], size=0, sort_term='asc')

    return request.chartsconfig.publication_article_authors(chart_data)


@view_config(route_name='publication_article_affiliations_map', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_article_affiliations_map(request):

    data = request.data_manager

    chart_data = request.stats.publication.general('article', 'aff_countries', data['selected_code'], data['selected_collection_code'], py_range=data['py_range'], sa_scope=data['sa_scope'], la_scope=data['la_scope'])

    return request.chartsconfig.publication_article_affiliations_map(chart_data)


@view_config(route_name='publication_article_affiliations', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_article_affiliations(request):

    data = request.data_manager

    chart_data = request.stats.publication.general('article', 'aff_countries', data['selected_code'], data['selected_collection_code'], py_range=data['py_range'], sa_scope=data['sa_scope'], la_scope=data['la_scope'], size=20)

    return request.chartsconfig.publication_article_affiliations(chart_data)


@view_config(route_name='publication_article_affiliations_publication_year', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_article_affiliations_publication_year(request):

    data = request.data_manager

    chart_data = request.stats.publication.affiliations_by_publication_year(data['selected_code'], data['selected_collection_code'], data['py_range'], data['sa_scope'], data['la_scope'])

    return request.chartsconfig.publication_article_affiliations_by_publication_year(chart_data)


@view_config(route_name='publication_article_year', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_article_year(request):

    data = request.data_manager

    data_chart = request.stats.publication.general('article', 'publication_year', data['selected_code'], data['selected_collection_code'], py_range=data['py_range'], sa_scope=data['sa_scope'], la_scope=data['la_scope'], size=0, sort_term='desc')

    return request.chartsconfig.publication_article_year(data_chart)


@view_config(route_name='publication_article_languages', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_article_languages(request):

    data = request.data_manager

    data_chart = request.stats.publication.general('article', 'languages', data['selected_code'], data['selected_collection_code'], py_range=data['py_range'], sa_scope=data['sa_scope'], la_scope=data['la_scope'])

    return request.chartsconfig.publication_article_languages(data_chart)


@view_config(route_name='publication_article_languages_publication_year', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_article_languages_publication_year(request):

    data = request.data_manager

    data_chart = request.stats.publication.languages_by_publication_year(data['selected_code'], data['selected_collection_code'], data['py_range'], data['sa_scope'], la_scope=data['la_scope'])

    return request.chartsconfig.publication_article_languages_by_publication_year(data_chart)


@view_config(route_name='publication_journal_status', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_journal_status(request):

    data = request.data_manager

    data_chart = request.stats.publication.general('journal', 'status', data['selected_code'], data['selected_collection_code'], sa_scope=data['sa_scope'])

    return request.chartsconfig.publication_journal_status(data_chart)


@view_config(route_name='publication_journal_year', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_journal_year(request):

    data = request.data_manager

    data_chart = request.stats.publication.general('journal', 'included_at_year', data['selected_code'], data['selected_collection_code'], sa_scope=data['sa_scope'], size=0, sort_term='asc')

    return request.chartsconfig.publication_journal_year(data_chart)


@view_config(route_name='publication_article_citable_documents', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_article_citable_documents(request):

    data = request.data_manager

    data_chart = request.stats.publication.citable_documents(data['selected_code'], data['selected_collection_code'], py_range=data['py_range'])

    return request.chartsconfig.publication_article_citable_documents(data_chart)


@view_config(route_name='publication_article_subject_areas', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_article_subject_areas(request):

    data = request.data_manager

    data_chart = request.stats.publication.general('article', 'subject_areas', data['selected_code'], data['selected_collection_code'], py_range=data['py_range'], sa_scope=data['sa_scope'], la_scope=data['la_scope'])

    return request.chartsconfig.publication_article_subject_areas(data_chart)


@view_config(route_name='publication_article_subject_areas_publication_year', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_article_subject_areas_publication_year(request):

    data = request.data_manager

    data_chart = request.stats.publication.subject_areas_by_publication_year(data['selected_code'], data['selected_collection_code'], data['py_range'], data['sa_scope'], la_scope=data['la_scope'])

    return request.chartsconfig.publication_article_subject_areas_by_publication_year(data_chart)


@view_config(route_name='publication_article_document_type', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_article_document_type(request):

    data = request.data_manager

    data_chart = request.stats.publication.general('article', 'document_type', data['selected_code'], data['selected_collection_code'], py_range=data['py_range'], sa_scope=data['sa_scope'], la_scope=data['la_scope'])

    return request.chartsconfig.publication_article_document_type(data_chart)


@view_config(route_name='publication_article_licenses_publication_year', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_article_licenses_publication_year(request):

    data = request.data_manager

    data_chart = request.stats.publication.lincenses_by_publication_year(data['selected_code'], data['selected_collection_code'], data['py_range'], data['sa_scope'], data['la_scope'])

    return request.chartsconfig.publication_article_licenses_by_publication_year(data_chart)


@view_config(route_name='publication_article_licenses', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_article_licenses(request):

    data = request.data_manager

    data_chart = request.stats.publication.general('article', 'license', data['selected_code'], data['selected_collection_code'], py_range=data['py_range'], sa_scope=data['sa_scope'])

    return request.chartsconfig.publication_article_licenses(data_chart)


@view_config(route_name='publication_journal_subject_areas', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_journal_subject_areas(request):

    data = request.data_manager

    data_chart = request.stats.publication.general('journal', 'subject_areas', data['selected_code'], data['selected_collection_code'], sa_scope=data['sa_scope'])

    return request.chartsconfig.publication_journal_subject_areas(data_chart)


@view_config(route_name='publication_journal_licenses', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_journal_licenses(request):

    data = request.data_manager

    data_chart = request.stats.publication.general('journal', 'license', data['selected_code'], data['selected_collection_code'], sa_scope=data['sa_scope'])

    return request.chartsconfig.publication_journal_licenses(data_chart)


@view_config(route_name='publication_size', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_size(request):

    data = request.data_manager

    field = request.GET.get('field', None)

    data = request.stats.publication.collection_size(data['selected_code'], data['selected_collection_code'], field, data['py_range'], data['sa_scope'], data['la_scope'])

    return data


@view_config(route_name='accesses_bymonthandyear', request_method='GET', renderer='jsonp')
@base_data_manager
def bymonthandyear(request):

    data = request.data_manager

    range_start = request.GET.get('range_start', None)
    range_end = request.GET.get('range_end', None)

    data_chart = request.stats.access.access_by_month_and_year(data['selected_code'], data['selected_collection_code'], data['py_range'], data['sa_scope'], data['la_scope'], range_start, range_end)

    return request.chartsconfig.bymonthandyear(data_chart)


@view_config(route_name='accesses_bydocumenttype', request_method='GET', renderer='jsonp')
@base_data_manager
def documenttype(request):

    data = request.data_manager

    range_start = request.GET.get('range_start', None)
    range_end = request.GET.get('range_end', None)

    data_chart = request.stats.access.access_by_document_type(data['selected_code'], data['selected_collection_code'], data['py_range'], data['sa_scope'], data['la_scope'], range_start, range_end)

    return request.chartsconfig.documenttype(data_chart)


@view_config(route_name='accesses_lifetime', request_method='GET', renderer='jsonp')
@base_data_manager
def lifetime(request):

    data = request.data_manager

    range_start = request.GET.get('range_start', None)
    range_end = request.GET.get('range_end', None)

    data_chart = request.stats.access.access_lifetime(data['selected_code'], data['selected_collection_code'], data['py_range'], data['sa_scope'], data['la_scope'], range_start, range_end)

    return request.chartsconfig.lifetime(data_chart)
