# coding: utf-8
import datetime

from pyramid.settings import aslist

from dogpile.cache import make_region

from analytics import utils
from analytics import choices
import re

cache_region = make_region(name='control_manager')


def current_url(current_url, data):

    params = {
        'collection': data.get('selected_collection_code', None),
        'journal': data.get('selected_journal_code', None),
        'py_range': '-'.join(data.get('py_range', None)),
        'document': data.get('selected_document_code', None),
        'range_start': data.get('range_start', None),
        'range_end': data.get('range_end', None)
    }

    # escopo de áreas temáticas
    sa_scope = '&'.join(['sa_scope=%s' % i for i in data.get('sa_scope', [])])

    # escopo de idiomas de publicação dos documentos
    la_scope = '&'.join(['la_scope=%s' % i for i in data.get('la_scope', [])])

    params_url = '&'.join(['%s=%s' % (k, v) for k, v in params.items() if v]+[sa_scope])

    url = '?'.join([current_url.split('?')[0], params_url])

    return url


def check_session(wrapped):
    """
        Decorator to check and update session attributes.
    """

    def check(request, *arg, **kwargs):
        collection = request.GET.get('collection', None)
        journal = request.GET.get('journal', None)
        document = request.GET.get('document', None)
        range_start = request.GET.get('range_start', None)
        under_development = request.GET.get('under_development', None)
        range_end = request.GET.get('range_end', None)
        py_range = request.GET.get('py_range', None)
        sa_scope = sorted([v for k, v in request.GET.items() if k == 'sa_scope'])
        la_scope = sorted([v for k, v in request.GET.items() if k == 'la_scope'])
        locale = request.GET.get('_LOCALE_', request.locale_name)

        if journal == 'clean' and 'journal' in request.session:
            del request.session['journal']
            journal = None
            if 'document' in request.session:
                del request.session['document']
                document = None

        if document == 'clean' and 'document' in request.session:
            del request.session['document']
            document = None

        session_under_development = request.session.get('under_development', None)
        session_collection = request.session.get('collection', None)
        session_journal = request.session.get('journal', None)
        session_document = request.session.get('document', None)
        session_range_start = request.session.get('range_start', None)
        session_range_end = request.session.get('range_end', None)
        session_py_range = request.session.get('py_range', None)
        session_sa_scope = sorted(request.session.get('sa_scope', []))
        session_la_scope = sorted(request.session.get('la_scope', []))
        session_locale = request.session.get('_LOCALE_', None)

        if collection and collection != session_collection:
            request.session['collection'] = collection
            if 'journal' in request.session:
                del request.session['journal']
        elif not session_collection:
            request.session['collection'] = 'scl'

        if under_development and under_development != session_under_development:
            request.session['under_development'] = under_development

        if journal and journal != session_journal:
            request.session['journal'] = journal

        if document and document != session_document:
            request.session['document'] = document
            request.session['journal'] = document[1:10]

        if range_start and range_start != session_range_start:
            request.session['range_start'] = range_start

        if range_end and range_end != session_range_end:
            request.session['range_end'] = range_end

        if py_range and py_range != session_py_range:
            request.session['py_range'] = py_range

        if sa_scope and sorted(sa_scope) != sorted(session_sa_scope):
            request.session['sa_scope'] = sorted(sa_scope)

        if la_scope and sorted(la_scope) != sorted(session_la_scope):
            request.session['la_scope'] = sorted(la_scope)

        if locale and locale != session_locale:
            request.session['_LOCALE_'] = locale

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
        def get_data_manager(collection, journal, document, range_start, range_end):
            code = document or journal or collection or code
            data = {}

            xylose_doc = request.stats.articlemeta.document(document, collection) if document else None

            if xylose_doc and xylose_doc.publisher_id:
                data['selected_document'] = xylose_doc
                data['selected_document_code'] = document
                journal = document[1:10]

            collections = request.stats.articlemeta.certified_collections()
            journals = request.stats.articlemeta.collections_journals(collection)
            selected_journal = journals.get(journal, None)
            selected_journal_code = journal if journal in journals else None

            today = datetime.datetime.now()
            y3 = today - datetime.timedelta(365*3)
            y2 = today - datetime.timedelta(365*2)
            y1 = today - datetime.timedelta(365*1)

            data.update({
                'collections': collections,
                'selected_code': code,
                'selected_journal': selected_journal,
                'selected_journal_code': selected_journal_code,
                'selected_document_code': document or None,
                'selected_collection': collections[collection],
                'selected_collection_code': collection,
                'journals': journals,
                'range_start': range_start,
                'range_end': range_end,
                'today': today.isoformat()[0:10],
                'y3': y3.isoformat()[0:10],
                'y2': y2.isoformat()[0:10],
                'y1': y1.isoformat()[0:10]
            })

            return data

        collection_code = request.session.get('collection', None)
        journal_code = request.session.get('journal', None)
        under_development = request.session.get('under_development', '')
        range_end = request.session.get('range_end', datetime.datetime.now().isoformat()[0:10])
        range_start = request.session.get('range_start', (datetime.datetime.now() - datetime.timedelta(365*3)).isoformat()[0:10])
        document_code = utils.REGEX_ARTICLE.match(request.session.get('document', ''))
        if document_code:
            document_code = document_code.string

        data = get_data_manager(collection_code, journal_code, document_code, range_start, range_end)
        data['locale'] = request.session.get('_LOCALE_', request.locale_name)
        data['under_development'] = [i for i in aslist(request.registry.settings.get('under_development', '')) if i != under_development]
        data['google_analytics_code'] = request.registry.settings.get('google_analytics_code', None)
        data['google_analytics_sample_rate'] = request.registry.settings.get('google_analytics_sample_rate', '100')
        data['subject_areas'] = request.stats.publication.list_subject_areas(data['selected_code'], data['selected_collection_code'])
        data['languages'] = [(i, choices.ISO_639_1.get(i.upper(), 'undefined')) for i in request.stats.publication.list_languages(data['selected_code'], data['selected_collection_code'])]
        data['publication_years'] = request.stats.publication.list_publication_years(data['selected_code'], data['selected_collection_code'])
        if len(data['publication_years']) == 0:
            data['publication_years'] = [str(datetime.datetime.now().year)]
        py = '-'.join([data['publication_years'][-1], data['publication_years'][0]])
        data['py_range'] = request.session.get('py_range', py).split('-')
        data['sa_scope'] = request.session.get('sa_scope', data['subject_areas'])
        data['la_scope'] = request.session.get('la_scope', [k for k, v in data['languages']])
        data['share_this_url'] = current_url(request.url, data)

        setattr(request, 'data_manager', data)

        return wrapped(request, *arg, **kwargs)

    wrapper.__doc__ = wrapped.__doc__

    return wrapper
