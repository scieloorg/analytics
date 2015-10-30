# coding: utf-8

def chartsconfig(request):
    return ChartsConfig(request)

class ChartsConfig(object):
    def __init__(self, request):
        self.request = request

    @property
    def _(self):
        return self.request.translate

    @property
    def highchart(self):

        _higchart = {
            'chart': {'type': 'line', 'backgroundColor': 'transparent'},
            'yAxis' : {'min': 0, 'labels' :{'format': '{value}'}},
            'legend': {'align': 'center', 'highlightSeries': {'enabled': True}},
            'credits': {'href': 'http://www.scielo.org', 'text': self._(u'Fuente: SciELO.org')}
        }

        return _higchart

    def bibliometrics_journal_self_citation(self, data):

        name = {'self_citations': self._(u'Auto citação'), 'citations': self._(u'Citações')}

        for i, serie in enumerate(data['series']):
            data['series'][i]['name'] = name[serie['id']]

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de citações e auto citações')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': None}
            }
        chart['legend'] = {'enabled': True}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de citações') }
        chart['tooltip'] = {
            'headerFormat': self._(u'Ano de publicação') + ' <strong>{point.key}</strong><br>',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> {series.name}: <strong>{point.y}</strong> ({point.percentage:.0f}%)<br/>'
        }
        chart['plotOptions'] = {
            'column': {
                'stacking': 'normal'
            }
        }

        return {'options': chart}

    def publication_article_citable_documents(self, data):

        name = {'citable_documents': self._(u'Documentos citáveis'), 'not_citable_documents': self._(u'Documentos não citáveis')}

        for i, serie in enumerate(data['series']):
            data['series'][i]['name'] = name[serie['id']]

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de documentos citáveis e não citáveis')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': None}
            }
        chart['legend'] = {'enabled': True}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos') }
        chart['tooltip'] = {
            'headerFormat': self._(u'Ano de publicação') + ' <strong>{point.key}</strong><br>',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> {series.name}: <strong>{point.y}</strong> ({point.percentage:.0f}%)<br/>'
        }
        chart['plotOptions'] = {
            'column': {
                'stacking': 'normal'
            }
        }

        return {'options': chart}

    def publication_article_references(self, data):

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de número de referências bibliográficas dos documentos')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': self._(u'Referências bibliográficas')}
            }
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos') }
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'%s documentos com %s referências bibliográficas' % ('<strong>{point.y}</strong>', '<strong>{point.category}</strong>')),
            'followPointer': True
        }
        
        return {'options': chart}

    def publication_article_authors(self, data):

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de número de autores dos documentos')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': self._(u'Número de autores')}
            }
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos') }
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'%s documentos com %s autores' % ('<strong>{point.y}</strong>', '<strong>{point.category}</strong>')),
            'followPointer': True
        }

        return {'options': chart}

    def publication_article_affiliations(self, data):

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
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'País de afiliação') + ' <strong>{point.category}</strong><br>' + self._(u'Documentos') + ': <strong>{point.y}</strong>',
            'followPointer': True
        }

        return {'options': chart}

    def publication_article_year(self, data):

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de ano de publicação dos documentos')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': self._(u'Ano de publicação')}
            }
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos') }
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Ano de publicação') + ' <strong>{point.category}</strong><br>' + self._(u'Documentos') + ': <strong>{point.y}</strong>',
            'followPointer': True
        }

        return {'options': chart}

    def publication_article_languages(self, data):

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
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Idioma do documento') + ' <strong>{point.category}</strong><br>' + self._(u'Documentos') + ': <strong>{point.y}</strong>',
            'followPointer': True
        }

        return {'options': chart}

    def publication_journal_status(self, data):

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
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Situação da publicação') + ' <strong>{point.category}</strong><br>' + self._(u'Periódicos') + ': <strong>{point.y}</strong>',
            'followPointer': True
        }

        return {'options': chart}

    def publication_journal_year(self, data):

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de periódicos por ano de inclusão no SciELO')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': self._(u'Ano de inclusão')}
            }
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de periódicos') }
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Ano de inclusão') + ' <strong>{point.category}</strong><br>' + self._(u'Periódicos') + ': <strong>{point.y}</strong>',
            'followPointer': True
        }

        return {'options': chart}

    def publication_article_subject_areas(self, data):

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
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Área temática') + ' <strong>{point.category}</strong><br>' + self._(u'Documentos') + ': <strong>{point.y}</strong>'
        }

        return {'options': chart}

    def publication_article_document_type(self, data):

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
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Tipo de documento') + ' <strong>{point.category}</strong><br>' + self._(u'Documentos') + ': <strong>{point.y}</strong>',
            'followPointer': True
        }

        return {'options': chart}

    def publication_article_licenses(self, data):

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de licença de uso dos documentos')}
        chart['xAxis'] = {
            'categories': [x.upper() for x in data['categories']],
            'title': {'text': self._(u'Licenças de uso')}
            }
        chart['plotOptions'] = {'series': {'colorByPoint': True}}
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos') }
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Licença') + ' <strong>{point.category}</strong><br>' + self._(u'Documentos') + ': <strong>{point.y}</strong>',
            'followPointer': True
        }

        return {'options': chart}

    def publication_journal_subject_areas(self, data):

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
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Área temática') + ' <strong>{point.category}</strong><br>' + self._(u'Periódicos') + ': <strong>{point.y}</strong>'
        }

        return {'options': chart}

    def publication_journal_licenses(self, data):

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de licença de uso dos periódicos')}
        chart['xAxis'] = {
            'categories': [x.upper() for x in data['categories']],
            'title': {'text': self._(u'Licenças de uso')}
            }
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['plotOptions'] = {'series': {'colorByPoint': True}}
        chart['yAxis']['title'] = {'text': self._(u'Número de periódicos') }
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Licença') + ' <strong>{point.category}</strong><br>' + self._(u'Periódicos') + ': <strong>{point.y}</strong>',
            'followPointer': True
        }

        return {'options': chart}

    def bymonthandyear(self, data):

        chart = self.highchart
        chart['title'] = {'text': self._(u'Total de acessos por ano e mês')}
        chart['xAxis'] = {'categories': data['categories']}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Acessos') }
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> {point.category}<br>' + self._(u'Acessos a') + ' <strong>{series.name}</strong>: {point.y}',
            'followPointer': True
        }

        return {'options': chart}

    def documenttype(self, data):

        chart = self.highchart
        chart['chart']['type'] = 'pie'
        chart['title'] = {'text': self._('Total de accessos por tipo de documento')}
        chart['series'] = data['series']
        chart['tooltip'] = {
                'headerFormat': '',
                'pointFormat': u'<span style="color:{point.color}">\u25CF</span> '+ self._(u'%s acessos a documentos do tipo %s' % ('<strong>{point.y}</strong>', '<strong>{point.name}</strong>')),
                'followPointer': True
            }

        return {'options': chart}

    def lifetime(self, data):

        charts = []
        for item in data:
            chart = self.highchart
            chart['chart']['type'] = 'column'
            chart['legend'] = {'enabled': False}
            chart['title'] = {'text': self._(u'Vida útil de artigos por número de acessos em ') + item['series'][0]['name']}
            chart['xAxis'] = {'categories': item['categories']}
            chart['series'] = item['series']
            chart['yAxis']['title'] = {'text': self._(u'Acessos') + item['series'][0]['name'] }
            chart['tooltip'] = {
                'headerFormat': '',
                'pointFormat': u'<span style="color:{point.color}">\u25CF</span> '+ self._(u'Ano de referência') +' <strong>{series.name}</strong><br>' + self._(u'%s acessos aos documentos do ano %s' % ('<strong>{point.y}</strong>', '<strong>{point.category}</strong>')),
                'followPointer': True
            }
            charts.append(chart)

        return charts
