# coding: utf-8
from pyramid.view import view_config

from dogpile.cache import make_region

from analytics.control_manager import base_data_manager


cache_region = make_region(name='views_ajax_cache')


# @view_config(route_name='bibliometrics_journal_jcr_eigen_factor_chart', request_method='GET', renderer='jsonp')
# @base_data_manager
# def bibliometrics_journal_jcr_eigen_factor_chart(request):

#     data = request.data_manager

#     data = request.stats.bibliometrics.jcr_eigen_factor(data['selected_journal_code'])

#     return request.chartsconfig.bibliometrics_jcr_eigen_factor(data)


# @view_config(route_name='bibliometrics_journal_jcr_received_citations_chart', request_method='GET', renderer='jsonp')
# @base_data_manager
# def bibliometrics_journal_jcr_received_citations_chart(request):

#     data = request.data_manager

#     data = request.stats.bibliometrics.jcr_received_citations(data['selected_journal_code'])

#     return request.chartsconfig.bibliometrics_jcr_received_citations(data)


# @view_config(route_name='bibliometrics_journal_jcr_average_impact_factor_percentile_chart', request_method='GET', renderer='jsonp')
# @base_data_manager
# def bibliometrics_journal_jcr_average_impact_factor_percentile_chart(request):

#     data = request.data_manager

#     data = request.stats.bibliometrics.jcr_average_impact_factor_percentile(data['selected_journal_code'])

#     return request.chartsconfig.bibliometrics_jcr_average_impact_factor_percentile(data)


# @view_config(route_name='bibliometrics_journal_jcr_impact_factor_chart', request_method='GET', renderer='jsonp')
# @base_data_manager
# def bibliometrics_journal_jcr_impact_factor_chart(request):

#     data = request.data_manager

#     data = request.stats.bibliometrics.jcr_impact_factor(data['selected_journal_code'])

#     return request.chartsconfig.bibliometrics_jcr_impact_factor(data)


@view_config(route_name='bibliometrics_journal_google_h5m5_chart', request_method='GET', renderer='jsonp')
@base_data_manager
def bibliometrics_journal_google_h5m5_chart(request):

    data = request.data_manager

    data = request.stats.bibliometrics.google_h5m5(data['selected_journal_code'])

    return request.chartsconfig.bibliometrics_google_h5m5(data)


@view_config(route_name='usage_report_chart', request_method='GET', renderer='jsonp')
@base_data_manager
def usage_report_chart(request):

    data = request.data_manager

    api_version = request.GET.get('api_version', 'v2')
    range_start = request.GET.get('range_start', None)
    range_end = request.GET.get('range_end', None)
    report_code = request.GET.get('report_code', 'tr_j1')
    selected_code = data['selected_code']
    selected_collection_code = data['selected_collection_code']

    data_chart = request.stats.usage.get_usage_report(
        issn = selected_code,
        collection = selected_collection_code,
        begin_date = range_start,
        end_date = range_end,
        report_code = report_code,
        api_version = api_version,
    )

    return request.chartsconfig.usage_report(data_chart)


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

    result = request.stats.publication.general('journal', 'status', data['selected_code'], data['selected_collection_code'], sa_scope=data['sa_scope'])

    return request.chartsconfig.publication_journal_status(result)


@view_config(route_name='publication_journal_status_detailde', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_journal_status_detailde(request):

    data = request.data_manager

    return request.stats.publication.journals_status_detailde(data['selected_collection_code'])


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


@view_config(route_name='publication_article_document_type_publication_year', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_article_document_type_publication_year(request):

    data = request.data_manager

    data_chart = request.stats.publication.document_type_by_publication_year(data['selected_code'], data['selected_collection_code'], data['py_range'], data['sa_scope'], la_scope=data['la_scope'])

    return request.chartsconfig.publication_article_document_type_by_publication_year(data_chart)


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
