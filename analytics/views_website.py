from pyramid.view import view_config
from pyramid.response import Response
import pyramid.httpexceptions as exc

from dogpile.cache import make_region

from analytics import utils

cache_region = make_region(name='views_website_cache')

def check_session(wrapped):
    """
        Decorator to check and update session attributes.
    """

    def check(request, *arg, **kwargs):
        collection = request.GET.get('collection', None)
        journal = request.GET.get('journal', None)
        document = request.GET.get('document', None)

        if journal == 'clean' and 'journal' in request.session:
            del(request.session['journal'])
            journal = None
            if 'document' in request.session:
                del(request.session['document'])
                document = None

        if document == 'clean' and 'document' in request.session:
            del(request.session['document'])
            document = None


        session_collection = request.session.get('collection', None)
        session_journal = request.session.get('journal', None)
        session_document = request.session.get('document', None)

        if collection and collection != session_collection:
            request.session['collection'] = collection
            if 'journal' in request.session:
                del(request.session['journal'])
        elif not session_collection:
            request.session['collection'] = 'scl'

        if journal and journal != session_journal:
            request.session['journal'] = journal

        if document and document != session_document:
            request.session['document'] = document

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
        def get_data_manager(collection, journal, document):
            code = document or journal or collection
            data = {}
            if document:
                data['selected_document'] = request.articlemeta.document(document, collection)
                data['selected_document_code'] = document
                journal = document[1:10]

            collections = request.articlemeta.certified_collections()
            journals = request.articlemeta.collections_journals(collection)
            selected_journal = journals.get(journal, None)
            selected_journal_code = journal if journal in journals else None

            data.update({
                'collections': collections,
                'selected_code': code,
                'selected_journal': selected_journal,
                'selected_journal_code': selected_journal_code,
                'selected_collection': collections[collection],
                'selected_collection_code': collection,
                'journals': journals
            })

            return data

        collection_code = request.session.get('collection', None)
        journal_code = request.session.get('journal', None)
        document_code = utils.REGEX_ARTICLE.match(request.GET.get('document', ''))
        if document_code:
            document_code = document_code.string

        data = get_data_manager(collection_code, journal_code, document_code)
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

    document = request.GET.get('document', None)
    collection = request.GET.get('collection', None)

    data = request.data_manager
    data['page'] = 'accesses'

    return data

@view_config(route_name='production_web', renderer='templates/website/production.mako')
@base_data_manager
def production(request):

    data = request.data_manager
    data['page'] = 'production'

    data['selected_code'] =  request.GET.get('code', data['selected_code'])

    return data