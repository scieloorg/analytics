from pyramid.view import view_config
from pyramid.response import Response
import pyramid.httpexceptions as exc

from dogpile.cache import make_region

cache_region = make_region(name='views_website_cache')

def check_session(wrapped):
    """
        Decorator to check and update session attributes.
    """

    def check(request, *arg, **kwargs):
        collection = request.GET.get('collection', None)
        journal = request.GET.get('journal', None)

        if journal == 'clean' and 'journal' in request.session:
            del(request.session['journal'])
            journal = None

        session_collection = request.session.get('collection', None)
        session_journal = request.session.get('journal', None)

        if collection and collection != session_collection:
            request.session['collection'] = collection
            if 'journal' in request.session:
                del(request.session['journal'])

        elif not session_collection:
            request.session['collection'] = 'scl'

        if journal and journal != session_journal:
            request.session['journal'] = journal

        return wrapped(request, *arg, **kwargs)

    check.__doc__ = wrapped.__doc__

    return check


def base_data_manager(wrapped):
    """
        Decorator to load common data used by all views
    """

    @check_session
    def wrapper(request, *arg, **kwargs):

        @cache_region.cache_on_arguments()
        def get_data_manager(collection, journal):
            code = journal or collection
            collections = request.articlemeta.certified_collections()
            journals = request.articlemeta.collections_journals(collection)
            selected_journal = journals.get(journal, None)
            selected_journal_code = journal if journal in journals else None

            data = {
                'collections': collections,
                'selected_code': code,
                'selected_journal': selected_journal,
                'selected_journal_code': selected_journal_code,
                'selected_collection': collections[collection],
                'selected_collection_code': collection,
                'journals': journals
            }

            return data            

        collection_code = request.session.get('collection', None)
        journal_code = request.session.get('journal', None)
        data = get_data_manager(collection_code, journal_code)
        setattr(request, 'data_manager', data)

        return wrapped(request, *arg, **kwargs)

    wrapper.__doc__ = wrapped.__doc__

    return wrapper

@view_config(route_name='index_web', renderer='templates/website/home.mako')
@base_data_manager
def index(request):
    data = request.data_manager
    data['page'] = 'home'

    return data

@view_config(route_name='accesses_web', renderer='templates/website/accesses.mako')
@base_data_manager
def accesses(request):

    data = request.data_manager
    data['page'] = 'accesses'

    return data

@view_config(route_name='production_web', renderer='templates/website/production.mako')
@base_data_manager
def production(request):

    data = request.data_manager
    data['page'] = 'production'

    return data