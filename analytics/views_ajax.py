from pyramid.view import view_config
from pyramid.response import Response
import pyramid.httpexceptions as exc


@view_config(route_name='bymonthandyear', request_method='GET', renderer='jsonp')
def bymonthandyear(request):

    collection = request.GET.get('collection', None)
    code = request.GET.get('code', None)

    data = request.accessstats.access_by_month_and_year(code, collection)

    return data