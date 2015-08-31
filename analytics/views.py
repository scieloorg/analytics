from pyramid.view import view_config
from pyramid.response import Response
import pyramid.httpexceptions as exc

@view_config(route_name='index_api', request_method='GET')
def index(request):
    return Response('Access Stats API by SciELO')


@view_config(route_name='stats', request_method='GET', renderer='jsonp')
def stats(request):

    collection = request.GET.get('collection', None)
    pid = request.GET.get('pid', None)
    issn = request.GET.get('issn', None)
    subject_area = request.GET.get('subject_area', None)
    affiliation_country = request.GET.get('affiliation_country', None)
    publication_year = request.GET.get('publication_year', None)
    document_type = request.GET.get('document_type', None)
    language = request.GET.get('language', None)
    aggs = request.GET.get('aggs', None)

    if not aggs:
        raise exc.HTTPBadRequest("aggs parameter is required")

    if len(aggs.split(',')) > 3:
        raise exc.HTTPBadRequest("max aggregations allowed is 3, you are must doing something wrong if you are trying to use more than 2 aggregations")

    filters = {}
    if collection:
        filters['collection'] = collection
    if issn:
        filters['issn'] = issn
    if subject_area:
        filters['subject_areas'] = subject_area
    if affiliation_country:
        filters['aff_countries'] = affiliation_country
    if publication_year:
        filters['publication_year'] = publication_year
    if document_type:
        filters['document_type'] = document_type
    if language:
        filters['languages'] = language
    if pid:
        filters['pid'] = pid

    try:
        data = request.index.access_stats(doc_type='articles', filters=filters, aggs=aggs.split(','))
    except ValueError as error:
        raise exc.HTTPBadRequest(error.message)

    return data

@view_config(route_name='document', request_method='GET', renderer='jsonp')
def document(request):

    collection = request.GET.get('collection', None)
    code = request.GET.get('code', None)

    if not collection:
        raise exc.HTTPBadRequest("collection parameter is required")

    if not code:
        raise exc.HTTPBadRequest("code parameter is required")

    try:
        data = request.index.document(code, collection)
    except ValueError as error:
        raise exc.HTTPBadRequest(error.message)

    return data