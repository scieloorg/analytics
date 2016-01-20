#coding: utf-8
from pyramid.view import view_config
from pyramid.response import Response
import pyramid.httpexceptions as exc

from dogpile.cache import make_region

from analytics.control_manager import base_data_manager, check_session
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

    data = request.stats.impact_factor_chart(data['selected_journal_code'], data['selected_collection_code'], titles)

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

    data = request.stats.received_self_and_granted_citation_chart(data['selected_journal_code'], data['selected_collection_code'], titles)

    return request.chartsconfig.bibliometrics_journal_received_self_and_granted_citation_chart(data)


class ViewsAjax(object):
    def __init__(self, request):
        self.request = request

    @property
    def _(self):
        return self.request.translate

    @property
    def collection(self):
        return self.request.GET.get('collection', None)

    @view_config(route_name='publication_article_references', request_method='GET', renderer='jsonp')
    def publication_article_references(self):

        code = self.request.GET.get('code', None)

        data = self.request.stats.publication.general('article', 'citations', code, self.collection, 40, 'asc')

        return self.request.chartsconfig.publication_article_references(data)

    @view_config(route_name='publication_article_authors', request_method='GET', renderer='jsonp')
    def publication_article_authors(self):

        code = self.request.GET.get('code', None)

        data = self.request.stats.publication.general('article', 'authors', code, self.collection, 0, 'asc')

        return self.request.chartsconfig.publication_article_authors(data)

    @view_config(route_name='publication_article_affiliations', request_method='GET', renderer='jsonp')
    def publication_article_affiliations(self):

        code = self.request.GET.get('code', None)

        data = self.request.stats.publication.general('article', 'aff_countries', code, self.collection, 20)

        return self.request.chartsconfig.publication_article_affiliations(data)

    @view_config(route_name='publication_article_affiliations_publication_year', request_method='GET', renderer='jsonp')
    def publication_article_affiliations_publication_year(self):

        code = self.request.GET.get('code', None)

        data = self.request.stats.publication.affiliations_by_publication_year(code, self.collection)

        return self.request.chartsconfig.publication_article_affiliations_by_publication_year(data)

    @view_config(route_name='publication_article_year', request_method='GET', renderer='jsonp')
    def publication_article_year(self):

        code = self.request.GET.get('code', None)

        data = self.request.stats.publication.general('article', 'publication_year', code, self.collection, 0, 'desc' )

        return self.request.chartsconfig.publication_article_year(data)


    @view_config(route_name='publication_article_languages', request_method='GET', renderer='jsonp')
    def publication_article_languages(self):

        code = self.request.GET.get('code', None)

        data = self.request.stats.publication.general('article', 'languages', code, self.collection)

        return self.request.chartsconfig.publication_article_languages(data)


    @view_config(route_name='publication_article_languages_publication_year', request_method='GET', renderer='jsonp')
    def publication_article_languages_publication_year(self):

        code = self.request.GET.get('code', None)

        data = self.request.stats.publication.languages_by_publication_year(code, self.collection)

        return self.request.chartsconfig.publication_article_languages_by_publication_year(data)

    @view_config(route_name='publication_journal_status', request_method='GET', renderer='jsonp')
    def publication_journal_status(self):

        code = self.request.GET.get('code', None)

        data = self.request.stats.publication.general('journal', 'status', code, self.collection)

        return self.request.chartsconfig.publication_journal_status(data)


    @view_config(route_name='publication_journal_year', request_method='GET', renderer='jsonp')
    def publication_journal_year(self):

        code = self.request.GET.get('code', None)

        data = self.request.stats.publication.general('journal', 'included_at_year', code, self.collection, 0, 'asc')

        return self.request.chartsconfig.publication_journal_year(data)


    @view_config(route_name='publication_article_citable_documents', request_method='GET', renderer='jsonp')
    def publication_article_citable_documents(self):

        code = self.request.GET.get('code', None)

        data = self.request.stats.publication.citable_documents(code, self.collection)

        return self.request.chartsconfig.publication_article_citable_documents(data)

    @view_config(route_name='publication_article_subject_areas', request_method='GET', renderer='jsonp')
    def publication_article_subject_areas(self):

        code = self.request.GET.get('code', None)

        data = self.request.stats.publication.general('article', 'subject_areas', code, self.collection)

        return self.request.chartsconfig.publication_article_subject_areas(data)


    @view_config(route_name='publication_article_subject_areas_publication_year', request_method='GET', renderer='jsonp')
    def publication_article_subject_areas_publication_year(self):
        code = self.request.GET.get('code', None)

        data = self.request.stats.publication.subject_areas_by_publication_year(code, self.collection)

        return self.request.chartsconfig.publication_article_subject_areas_by_publication_year(data)


    @view_config(route_name='publication_article_document_type', request_method='GET', renderer='jsonp')
    def publication_article_document_type(self):

        code = self.request.GET.get('code', None)

        data = self.request.stats.publication.general('article', 'document_type', code, self.collection)

        return self.request.chartsconfig.publication_article_document_type(data)

    @view_config(route_name='publication_article_licenses_publication_year', request_method='GET', renderer='jsonp')
    def publication_article_licenses_publication_year(self):

        code = self.request.GET.get('code', None)

        data = self.request.stats.publication.lincenses_by_publication_year(code, self.collection)

        return self.request.chartsconfig.publication_article_licenses_by_publication_year(data)

    @view_config(route_name='publication_article_licenses', request_method='GET', renderer='jsonp')
    def publication_article_licenses(self):

        code = self.request.GET.get('code', None)

        data = self.request.stats.publication.general('article', 'license', code, self.collection)

        return self.request.chartsconfig.publication_article_licenses(data)


    @view_config(route_name='publication_journal_subject_areas', request_method='GET', renderer='jsonp')
    def publication_journal_subject_areas(self):

        code = self.request.GET.get('code', None)

        data = self.request.stats.publication.general('journal', 'subject_areas', code, self.collection)

        return self.request.chartsconfig.publication_journal_subject_areas(data)


    @view_config(route_name='publication_journal_licenses', request_method='GET', renderer='jsonp')
    def publication_journal_licenses(self):

        code = self.request.GET.get('code', None)

        data = self.request.stats.publication.general('journal', 'license', code, self.collection)

        return self.request.chartsconfig.publication_journal_licenses(data)

    @view_config(route_name='publication_size', request_method='GET', renderer='jsonp')
    def publication_size(self):

        code = self.request.GET.get('code', None)
        field = self.request.GET.get('field', None)

        data = self.request.stats.publication.collection_size(code, self.collection, field)

        return data

    @view_config(route_name='accesses_bymonthandyear', request_method='GET', renderer='jsonp')
    def bymonthandyear(self):

        code = self.request.GET.get('code', None)
        range_start = self.request.GET.get('range_start', None)
        range_end = self.request.GET.get('range_end', None)

        data = self.request.stats.access.access_by_month_and_year(code, self.collection, range_start, range_end)
        
        return self.request.chartsconfig.bymonthandyear(data)


    @view_config(route_name='accesses_bydocumenttype', request_method='GET', renderer='jsonp')
    def documenttype(self):

        code = self.request.GET.get('code', None)
        range_start = self.request.GET.get('range_start', None)
        range_end = self.request.GET.get('range_end', None)

        data = self.request.stats.access.access_by_document_type(code, self.collection, range_start, range_end)

        return self.request.chartsconfig.documenttype(data)


    @view_config(route_name='accesses_lifetime', request_method='GET', renderer='jsonp')
    def lifetime(self):

        code = self.request.GET.get('code', None)
        range_start = self.request.GET.get('range_start', None)
        range_end = self.request.GET.get('range_end', None)

        data = self.request.stats.access.access_lifetime(code, self.collection, range_start, range_end)

        return self.request.chartsconfig.lifetime(data)
