# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.response import Response
import pyramid.httpexceptions as exc

class ViewsAjax(object):
    def __init__(self, request):
        self.request = request

    @property
    def _(self):
        return self.request.translate

    @property
    def collection(self):
        return self.request.GET.get('collection', None)

    @property
    def highchart(self):
        _higchart = {
            'chart': {'type': 'line', 'backgroundColor': 'transparent'},
            'credits': {'href': 'http://www.scielo.org', 'text': (u'Fuente: SciELO.org')},
            'yAxis' : {'min': 0, 'labels' :{'format': '{value}'}},
            'legend': {'align': 'center', 'highlightSeries': {'enabled': True}},
            'credits': {'href': 'http://www.scielo.org', 'text': self._(u'Fuente: SciELO.org')}
        }
        return _higchart

    @view_config(route_name='publication_article_references', request_method='GET', renderer='jsonp')
    def publication_article_references(self):

        code = self.request.GET.get('code', None)

        data = self.request.publicationstats.general('article', 'citations', code, self.collection, 40)

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de número de referências bibliográficas dos documentos')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': self._(u'Referências bibliográficas')}
            }
        chart['plotOptions'] = {'series': {'colorByPoint': True}}
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos') }
        return {'options': chart}

    @view_config(route_name='publication_article_authors', request_method='GET', renderer='jsonp')
    def publication_article_authors(self):

        code = self.request.GET.get('code', None)

        data = self.request.publicationstats.general('article', 'authors', code, self.collection)

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de número de autores dos documentos')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': self._(u'Número de autores')}
            }
        chart['plotOptions'] = {'series': {'colorByPoint': True}}
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos') }
        return {'options': chart}

    @view_config(route_name='publication_article_affiliations', request_method='GET', renderer='jsonp')
    def publication_article_affiliations(self):

        code = self.request.GET.get('code', None)

        data = self.request.publicationstats.general('article', 'aff_countries', code, self.collection, 20)

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de países de afiliação dos documentos')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': self._(u'País de afiliação')}
            }
        chart['plotOptions'] = {'series': {'colorByPoint': True}}
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos') }
        return {'options': chart}


    @view_config(route_name='publication_article_year', request_method='GET', renderer='jsonp')
    def publication_article_year(self):

        code = self.request.GET.get('code', None)

        data = self.request.publicationstats.general('article', 'publication_year', code, self.collection)

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de ano de publicação dos documentos')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': self._(u'Ano de publicação')}
            }
        chart['plotOptions'] = {'series': {'colorByPoint': True}}
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos') }
        return {'options': chart}


    @view_config(route_name='publication_article_languages', request_method='GET', renderer='jsonp')
    def publication_article_languages(self):

        code = self.request.GET.get('code', None)

        data = self.request.publicationstats.general('article', 'languages', code, self.collection)

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de idiomas dos documentos')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': self._(u'Idiomas de publicação')}
            }
        chart['plotOptions'] = {'series': {'colorByPoint': True}}
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos') }
        return {'options': chart}


    @view_config(route_name='publication_journal_status', request_method='GET', renderer='jsonp')
    def publication_journal_status(self):

        code = self.request.GET.get('code', None)

        data = self.request.publicationstats.general('journal', 'status', code, self.collection)

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de periódicos por situação atual de publicação no SciELO')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': self._(u'Situação da publicação')}
            }
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['plotOptions'] = {'series': {'colorByPoint': True}}
        chart['yAxis']['title'] = {'text': self._(u'Número de periódicos') }
        return {'options': chart}


    @view_config(route_name='publication_journal_year', request_method='GET', renderer='jsonp')
    def publication_journal_year(self):

        code = self.request.GET.get('code', None)

        data = self.request.publicationstats.general('journal', 'included_at_year', code, self.collection)

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de periódicos por ano de inclusão no SciELO')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': self._(u'Ano de inclusão')}
            }
        chart['plotOptions'] = {'series': {'colorByPoint': True}}
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de periódicos') }
        return {'options': chart}


    @view_config(route_name='publication_article_subject_areas', request_method='GET', renderer='jsonp')
    def publication_article_subject_areas(self):

        code = self.request.GET.get('code', None)

        data = self.request.publicationstats.general('article', 'subject_areas', code, self.collection)

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de área temática dos documentos')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': self._(u'Areas temáticas')}
            }
        chart['plotOptions'] = {'series': {'colorByPoint': True}}
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos') }
        return {'options': chart}


    @view_config(route_name='publication_article_document_type', request_method='GET', renderer='jsonp')
    def publication_article_document_type(self):

        code = self.request.GET.get('code', None)

        data = self.request.publicationstats.general('article', 'document_type', code, self.collection)

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição por tipo de documento')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': self._(u'Tipos de documentos')}
            }
        chart['plotOptions'] = {'series': {'colorByPoint': True}}
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos') }
        return {'options': chart}

    @view_config(route_name='publication_article_licenses', request_method='GET', renderer='jsonp')
    def publication_article_licenses(self):

        code = self.request.GET.get('code', None)

        data = self.request.publicationstats.general('article', 'license', code, self.collection)

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de licença de uso dos documentos')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': self._(u'Licenças de uso')}
            }
        chart['plotOptions'] = {'series': {'colorByPoint': True}}
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos') }
        return {'options': chart}


    @view_config(route_name='publication_journal_subject_areas', request_method='GET', renderer='jsonp')
    def publication_journal_subject_areas(self):

        code = self.request.GET.get('code', None)

        data = self.request.publicationstats.general('journal', 'subject_areas', code, self.collection)

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de área temática dos periódicos')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': self._(u'Areas temáticas')}
            }
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['plotOptions'] = {'series': {'colorByPoint': True}}
        chart['yAxis']['title'] = {'text': self._(u'Número de periódicos') }
        return {'options': chart}


    @view_config(route_name='publication_journal_licenses', request_method='GET', renderer='jsonp')
    def publication_journal_licenses(self):

        code = self.request.GET.get('code', None)

        data = self.request.publicationstats.general('journal', 'license', code, self.collection)

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de licença de uso dos periódicos')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': self._(u'Licenças de uso')}
            }
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['plotOptions'] = {'series': {'colorByPoint': True}}
        chart['yAxis']['title'] = {'text': self._(u'Número de periódicos') }
        return {'options': chart}

    @view_config(route_name='accesses_bymonthandyear', request_method='GET', renderer='jsonp')
    def bymonthandyear(self):

        code = self.request.GET.get('code', None)
        range_start = self.request.GET.get('range_start', None)
        range_end = self.request.GET.get('range_end', None)

        data = self.request.accessstats.access_by_month_and_year(code, self.collection, range_start, range_end)
        
        chart = self.highchart
        chart['title'] = {'text': self._(u'Total de acessos por ano e mês')}
        chart['xAxis'] = {'categories': data['categories']}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Acessos') }
        return {'options': chart}


    @view_config(route_name='accesses_bydocumenttype', request_method='GET', renderer='jsonp')
    def documenttype(self):

        code = self.request.GET.get('code', None)
        range_start = self.request.GET.get('range_start', None)
        range_end = self.request.GET.get('range_end', None)

        data = self.request.accessstats.access_by_document_type(code, self.collection, range_start, range_end)

        chart = self.highchart
        chart['chart']['type'] = 'pie'
        chart['title'] = {'text': self._('Total de accessos por tipo de documento')}
        chart['series'] = data['series']
        return {'options': chart}


    @view_config(route_name='accesses_lifetime', request_method='GET', renderer='jsonp')
    def lifetime(self):

        code = self.request.GET.get('code', None)
        range_start = self.request.GET.get('range_start', None)
        range_end = self.request.GET.get('range_end', None)

        data = self.request.accessstats.access_lifetime(code, self.collection, range_start, range_end)

        charts = []
        for item in data:
            chart = self.highchart
            chart['chart']['type'] = 'column'
            chart['legend'] = {'enabled': False}
            chart['title'] = {'text': self._(u'Vida útil de artigos por número de acessos em ') + item['series'][0]['name']}
            chart['xAxis'] = {'categories': item['categories']}
            chart['series'] = item['series']
            chart['yAxis']['title'] = {'text': self._(u'Acessos') + item['series'][0]['name'] }
            charts.append(chart)
        return charts
