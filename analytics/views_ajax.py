from pyramid.view import view_config
from pyramid.response import Response
import pyramid.httpexceptions as exc


@view_config(route_name='publication_article_references', request_method='GET', renderer='jsonp')
def publication_article_references(request):

    collection = request.GET.get('collection', None)
    code = request.GET.get('code', None)

    data = request.publicationstats.general('article', 'citations', code, collection, 40)

    return data

@view_config(route_name='publication_article_authors', request_method='GET', renderer='jsonp')
def publication_article_authors(request):

    collection = request.GET.get('collection', None)
    code = request.GET.get('code', None)

    data = request.publicationstats.general('article', 'authors', code, collection)

    return data

@view_config(route_name='publication_article_affiliations', request_method='GET', renderer='jsonp')
def publication_article_affiliations(request):

    collection = request.GET.get('collection', None)
    code = request.GET.get('code', None)

    data = request.publicationstats.general('article', 'aff_countries', code, collection, 20)

    return data


@view_config(route_name='publication_article_year', request_method='GET', renderer='jsonp')
def publication_article_year(request):

    collection = request.GET.get('collection', None)
    code = request.GET.get('code', None)

    data = request.publicationstats.general('article', 'publication_year', code, collection)

    return data


@view_config(route_name='publication_article_languages', request_method='GET', renderer='jsonp')
def publication_article_languages(request):

    collection = request.GET.get('collection', None)
    code = request.GET.get('code', None)

    data = request.publicationstats.general('article', 'languages', code, collection)

    return data


@view_config(route_name='publication_journal_status', request_method='GET', renderer='jsonp')
def publication_journal_status(request):

    collection = request.GET.get('collection', None)
    code = request.GET.get('code', None)

    data = request.publicationstats.general('journal', 'status', code, collection)

    return data


@view_config(route_name='publication_journal_year', request_method='GET', renderer='jsonp')
def publication_journal_year(request):

    collection = request.GET.get('collection', None)
    code = request.GET.get('code', None)

    data = request.publicationstats.general('journal', 'included_at_year', code, collection)

    return data


@view_config(route_name='publication_article_subject_areas', request_method='GET', renderer='jsonp')
def publication_article_subject_areas(request):

    collection = request.GET.get('collection', None)
    code = request.GET.get('code', None)

    data = request.publicationstats.general('article', 'subject_areas', code, collection)

    return data


@view_config(route_name='publication_article_document_type', request_method='GET', renderer='jsonp')
def publication_article_document_type(request):

    collection = request.GET.get('collection', None)
    code = request.GET.get('code', None)

    data = request.publicationstats.general('article', 'document_type', code, collection)

    return data

@view_config(route_name='publication_article_licenses', request_method='GET', renderer='jsonp')
def publication_article_licenses(request):

    collection = request.GET.get('collection', None)
    code = request.GET.get('code', None)

    data = request.publicationstats.general('article', 'license', code, collection)

    return data


@view_config(route_name='publication_journal_subject_areas', request_method='GET', renderer='jsonp')
def publication_journal_subject_areas(request):

    collection = request.GET.get('collection', None)
    code = request.GET.get('code', None)

    data = request.publicationstats.general('journal', 'subject_areas', code, collection)

    return data


@view_config(route_name='publication_journal_licenses', request_method='GET', renderer='jsonp')
def publication_journal_licenses(request):

    collection = request.GET.get('collection', None)
    code = request.GET.get('code', None)

    data = request.publicationstats.general('journal', 'license', code, collection)

    return data

@view_config(route_name='accesses_bymonthandyear', request_method='GET', renderer='jsonp')
def bymonthandyear(request):

    collection = request.GET.get('collection', None)
    code = request.GET.get('code', None)
    range_start = request.GET.get('range_start', None)
    range_end = request.GET.get('range_end', None)

    data = request.accessstats.access_by_month_and_year(code, collection, range_start, range_end)

    return data


@view_config(route_name='accesses_bydocumenttype', request_method='GET', renderer='jsonp')
def documenttype(request):

    collection = request.GET.get('collection', None)
    code = request.GET.get('code', None)
    range_start = request.GET.get('range_start', None)
    range_end = request.GET.get('range_end', None)

    data = request.accessstats.access_by_document_type(code, collection, range_start, range_end)

    return data


@view_config(route_name='accesses_lifetime', request_method='GET', renderer='jsonp')
def lifetime(request):

    collection = request.GET.get('collection', None)
    code = request.GET.get('code', None)
    range_start = request.GET.get('range_start', None)
    range_end = request.GET.get('range_end', None)

    data = request.accessstats.access_lifetime(code, collection, range_start, range_end)

    return data
