# coding: utf-8
import urllib.parse
import json
import logging
import os
import datetime
import threading
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FuturesTimeoutError

from pyramid.view import view_config

from dogpile.cache import make_region

from analytics.control_manager import base_data_manager, check_session
from analytics import request_utils
from analytics import monitoring
from analytics.controller import SCIELO_SUSHI_API_FETCH_DATA_TIMEOUT, SCIELO_SUSHI_API_ERROR_KEY, SCIELO_SUSHI_API_ERROR_VALUE


cache_region = make_region(name='views_ajax_cache')
logger = logging.getLogger(__name__)

_AFFILIATIONS_TIMEOUT_SECONDS = float(os.environ.get("PUBLICATION_AFFILIATIONS_TIMEOUT_SECONDS", "4"))
_AFFILIATIONS_TIMEOUT_POOL_SIZE = int(os.environ.get("PUBLICATION_AFFILIATIONS_TIMEOUT_POOL_SIZE", "8"))
_USAGE_REPORT_TIMEOUT_SECONDS = float(os.environ.get("USAGE_REPORT_TIMEOUT_SECONDS", "4"))
_USAGE_YEARLY_TIMEOUT_SECONDS = float(
    os.environ.get("USAGE_YEARLY_TIMEOUT_SECONDS", str(_USAGE_REPORT_TIMEOUT_SECONDS))
)
_USAGE_YEARLY_DEFAULT_MONTHS = int(os.environ.get("USAGE_YEARLY_DEFAULT_MONTHS", "24"))
_USAGE_TIMEOUT_POOL_SIZE = int(os.environ.get("USAGE_TIMEOUT_POOL_SIZE", "8"))
_USAGE_MAX_INFLIGHT = int(os.environ.get("USAGE_TIMEOUT_MAX_INFLIGHT", str(_USAGE_TIMEOUT_POOL_SIZE)))
_PUBLICATION_MAX_INFLIGHT = int(
    os.environ.get("PUBLICATION_AFFILIATIONS_MAX_INFLIGHT", str(_AFFILIATIONS_TIMEOUT_POOL_SIZE))
)

_USAGE_EXECUTOR = ThreadPoolExecutor(
    max_workers=_USAGE_TIMEOUT_POOL_SIZE,
    thread_name_prefix="usage-timeout",
)
_PUBLICATION_EXECUTOR = ThreadPoolExecutor(
    max_workers=_AFFILIATIONS_TIMEOUT_POOL_SIZE,
    thread_name_prefix="publication-timeout",
)
_USAGE_INFLIGHT = threading.BoundedSemaphore(value=_USAGE_MAX_INFLIGHT)
_PUBLICATION_INFLIGHT = threading.BoundedSemaphore(value=_PUBLICATION_MAX_INFLIGHT)


def _usage_cache_key(prefix, payload):
    return "%s:%s" % (
        prefix,
        json.dumps(payload, sort_keys=True, separators=(",", ":"))
    )


def _submit_guarded(executor, inflight_guard, callable_obj, operation_name):
    if not inflight_guard.acquire(blocking=False):
        logger.warning(
            "Inflight guard reached for %s; returning fallback without backend call",
            operation_name
        )
        backend = "usage" if operation_name.startswith("usage_") else "publication"
        monitoring.BACKEND_INFLIGHT_REJECTED_TOTAL.labels(backend=backend, operation=operation_name).inc()
        return None

    try:
        future = executor.submit(callable_obj)
    except Exception:
        inflight_guard.release()
        raise

    def _release_guard(_):
        try:
            inflight_guard.release()
        except ValueError:
            logger.warning("Inflight guard release imbalance for %s", operation_name)

    future.add_done_callback(_release_guard)
    return future


def _run_with_timeout(executor, inflight_guard, callable_obj, fallback_data, timeout_seconds, operation_name):
    backend = "usage" if operation_name.startswith("usage_") else "publication"
    future = _submit_guarded(executor, inflight_guard, callable_obj, operation_name)
    if future is None:
        monitoring.BACKEND_CALLS_TOTAL.labels(backend=backend, operation=operation_name, result="inflight_rejected").inc()
        return fallback_data

    try:
        started_at = datetime.datetime.now().timestamp()
        result = future.result(timeout=timeout_seconds)
        monitoring.BACKEND_CALLS_TOTAL.labels(backend=backend, operation=operation_name, result="success").inc()
        monitoring.BACKEND_CALL_DURATION_SECONDS.labels(backend=backend, operation=operation_name).observe(
            datetime.datetime.now().timestamp() - started_at
        )
        return result
    except FuturesTimeoutError:
        future.cancel()
        logger.warning(
            "Timeout in %s after %.2fs; returning fallback",
            operation_name,
            timeout_seconds
        )
        monitoring.BACKEND_CALLS_TOTAL.labels(backend=backend, operation=operation_name, result="timeout").inc()
        return fallback_data
    except Exception as exc:
        logger.warning(
            "Error in %s: %s; returning fallback",
            operation_name,
            exc
        )
        monitoring.BACKEND_CALLS_TOTAL.labels(backend=backend, operation=operation_name, result="error").inc()
        return fallback_data


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


def _usage_selected_values(request):
    selected_collection_code = (
        request.GET.get('collection')
        or request.session.get('collection')
        or 'scl'
    )
    selected_document_code = (
        request.GET.get('pid')
        or request.GET.get('article')
        or request.session.get('document')
        or None
    )
    selected_code = (
        request.GET.get('issn')
        or request.GET.get('code')
        or request.GET.get('journal')
        or request.session.get('journal')
        or selected_collection_code
    )
    return selected_code, selected_collection_code, selected_document_code


def _usage_date_range(request):
    today = datetime.datetime.now().isoformat()[0:10]
    range_start = (
        request.GET.get('range_start')
        or request.session.get('range_start')
        or '1998-01-01'
    )
    range_end = (
        request.GET.get('range_end')
        or request.session.get('range_end')
        or today
    )
    return range_start, range_end


def _subtract_months(yyyy_mm_dd, months):
    year, month, _ = [int(x) for x in yyyy_mm_dd.split('-')]
    total = (year * 12 + (month - 1)) - months
    new_year = total // 12
    new_month = (total % 12) + 1
    return "%04d-%02d-01" % (new_year, new_month)


def _usage_yearly_date_range(request):
    # Preserve explicit user filters from query string.
    if request.GET.get('range_start') and request.GET.get('range_end'):
        return request.GET.get('range_start'), request.GET.get('range_end')

    today = datetime.datetime.now().isoformat()[0:10]
    range_end = request.GET.get('range_end') or request.session.get('range_end') or today
    range_start = request.GET.get('range_start') or request.session.get('range_start')

    if range_start:
        return range_start, range_end

    return _subtract_months(range_end, _USAGE_YEARLY_DEFAULT_MONTHS), range_end


@view_config(route_name='usage_report_chart', request_method='GET', renderer='jsonp')
@check_session
def usage_report_chart(request):

    api_version = request.GET.get('api_version', 'v2')
    range_start, range_end = _usage_date_range(request)
    report_code = request.GET.get('report_code', 'tr_j1')
    granularity = request.GET.get('granularity', 'monthly')
    selected_code, selected_collection_code, selected_document_code = _usage_selected_values(request)

    cache_payload = {
        'pid': selected_document_code,
        'issn': selected_code,
        'collection': selected_collection_code,
        'begin_date': range_start,
        'end_date': range_end,
        'report_code': report_code,
        'api_version': api_version,
        'granularity': granularity,
    }
    cache_key = _usage_cache_key("usage_report_chart", cache_payload)

    fallback_data = []
    if report_code != 'gr_j1':
        fallback_data = {'series': []}

    data_chart = _run_with_timeout(
        _USAGE_EXECUTOR,
        _USAGE_INFLIGHT,
        lambda: cache_region.get_or_create(
            cache_key,
            lambda: request.stats.usage.get_usage_report(
                pid=selected_document_code,
                issn=selected_code,
                collection=selected_collection_code,
                begin_date=range_start,
                end_date=range_end,
                report_code=report_code,
                api_version=api_version,
                granularity=granularity,
            )
        )
        ,
        fallback_data=fallback_data,
        timeout_seconds=_USAGE_REPORT_TIMEOUT_SECONDS,
        operation_name='usage_report_chart',
    )

    if report_code == 'gr_j1':
        return request.chartsconfig.usage_report_geolocation(data_chart)

    return request.chartsconfig.usage_report(data_chart)


@view_config(route_name='usage_report_yearly_chart', request_method='GET', renderer='jsonp')
@check_session
def usage_report_yearly_chart(request):

    api_version = request.GET.get('api_version', 'v2')
    range_start, range_end = _usage_yearly_date_range(request)
    report_code = request.GET.get('report_code', 'cr_j1')
    metric_type = request.GET.get('metric_type', 'Total_Item_Requests')
    selected_code, selected_collection_code, selected_document_code = _usage_selected_values(request)
    
    cache_payload = {
        'pid': selected_document_code,
        'issn': selected_code,
        'collection': selected_collection_code,
        'begin_date': range_start,
        'end_date': range_end,
        'report_code': report_code,
        'api_version': api_version,
        'metric_type': metric_type,
        'granularity': 'monthly',
    }
    cache_key = _usage_cache_key("usage_report_yearly_chart", cache_payload)

    def _compute_yearly_chart():
        url_report = urllib.parse.urljoin(request.stats.usage.base_url, 'reports/%s' % report_code)

        params = {
            'pid': selected_document_code,
            'issn': selected_code,
            'collection': selected_collection_code,
            'begin_date': range_start,
            'end_date': range_end,
            'granularity': 'monthly',
            'api': api_version,
        }

        request_utils.clean_params_by_report(params, report_code)

        try:
            data_raw = request_utils.fetch_data(
                url_report,
                params=params,
                timeout=SCIELO_SUSHI_API_FETCH_DATA_TIMEOUT,
            )
        except (request_utils.RetryableError, request_utils.NonRetryableError):
            return {'series': [], 'categories': []}

        severity = data_raw.get(SCIELO_SUSHI_API_ERROR_KEY, '')
        if isinstance(severity, str) and severity.lower() == SCIELO_SUSHI_API_ERROR_VALUE.lower():
            return {'series': [], 'categories': []}

        return request.stats.usage._title_report_to_yearly_chart_data(data_raw, metric_type=metric_type)

    data_chart = _run_with_timeout(
        _USAGE_EXECUTOR,
        _USAGE_INFLIGHT,
        lambda: cache_region.get_or_create(cache_key, _compute_yearly_chart),
        fallback_data={'series': [], 'categories': []},
        timeout_seconds=_USAGE_YEARLY_TIMEOUT_SECONDS,
        operation_name='usage_report_yearly_chart',
    )
    
    return request.chartsconfig.usage_report_yearly(data_chart, metric_type)



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

    cache_payload = {
        'selected_code': data['selected_code'],
        'selected_collection_code': data['selected_collection_code'],
        'py_range': data['py_range'],
        'sa_scope': data['sa_scope'],
        'la_scope': data['la_scope'],
    }
    cache_key = _usage_cache_key("publication_article_affiliations_map", cache_payload)

    chart_data = _run_with_timeout(
        _PUBLICATION_EXECUTOR,
        _PUBLICATION_INFLIGHT,
        lambda: cache_region.get_or_create(
            cache_key,
            lambda: request.stats.publication.general(
                'article',
                'aff_countries',
                data['selected_code'],
                data['selected_collection_code'],
                py_range=data['py_range'],
                sa_scope=data['sa_scope'],
                la_scope=data['la_scope'],
            )
        ),
        fallback_data={'series': [{'name': 'documents', 'data': []}], 'categories': []},
        timeout_seconds=_AFFILIATIONS_TIMEOUT_SECONDS,
        operation_name='publication_article_affiliations_map',
    )

    return request.chartsconfig.publication_article_affiliations_map(chart_data)


@view_config(route_name='publication_article_affiliations', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_article_affiliations(request):

    data = request.data_manager

    cache_payload = {
        'selected_code': data['selected_code'],
        'selected_collection_code': data['selected_collection_code'],
        'py_range': data['py_range'],
        'sa_scope': data['sa_scope'],
        'la_scope': data['la_scope'],
        'size': 20,
    }
    cache_key = _usage_cache_key("publication_article_affiliations", cache_payload)

    chart_data = _run_with_timeout(
        _PUBLICATION_EXECUTOR,
        _PUBLICATION_INFLIGHT,
        lambda: cache_region.get_or_create(
            cache_key,
            lambda: request.stats.publication.general(
                'article',
                'aff_countries',
                data['selected_code'],
                data['selected_collection_code'],
                py_range=data['py_range'],
                sa_scope=data['sa_scope'],
                la_scope=data['la_scope'],
                size=20,
            )
        )
        ,
        fallback_data={'series': [{'name': 'documents', 'data': []}], 'categories': []},
        timeout_seconds=_AFFILIATIONS_TIMEOUT_SECONDS,
        operation_name='publication_article_affiliations',
    )

    return request.chartsconfig.publication_article_affiliations(chart_data)


@view_config(route_name='publication_article_affiliations_publication_year', request_method='GET', renderer='jsonp')
@base_data_manager
def publication_article_affiliations_publication_year(request):

    data = request.data_manager

    cache_payload = {
        'selected_code': data['selected_code'],
        'selected_collection_code': data['selected_collection_code'],
        'py_range': data['py_range'],
        'sa_scope': data['sa_scope'],
        'la_scope': data['la_scope'],
    }
    cache_key = _usage_cache_key("publication_article_affiliations_publication_year", cache_payload)

    chart_data = _run_with_timeout(
        _PUBLICATION_EXECUTOR,
        _PUBLICATION_INFLIGHT,
        lambda: cache_region.get_or_create(
            cache_key,
            lambda: request.stats.publication.affiliations_by_publication_year(
                data['selected_code'],
                data['selected_collection_code'],
                data['py_range'],
                data['sa_scope'],
                data['la_scope']
            )
        )
        ,
        fallback_data={'series': [], 'navigator_series': []},
        timeout_seconds=_AFFILIATIONS_TIMEOUT_SECONDS,
        operation_name='publication_article_affiliations_publication_year',
    )

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
