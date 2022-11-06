# coding: utf-8

from analytics import choices


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

        _highchart = {
            'chart': {'type': 'line', 'backgroundColor': '#FFFFFF'},
            'yAxis': {'min': 0, 'labels': {'format': '{value}'}},
            'legend': {'align': 'center', 'highlightSeries': {'enabled': True}},
            'credits': {'href': 'http://www.scielo.org', 'text': self._(u'Fonte: SciELO.org')}
        }

        return _highchart

    # def access_heat(self, data):

    #     chart = self.highchart

    #     chart['chart']['type'] = 'heatmap'
    #     chart['xAxis'] = {'categories': data['categories_x']}
    #     chart['yAxis'] = {'categories': data['categories_y']}
    #     chart['series'] = [{'data': data['series']}]
    #     chart['colorAxis'] = {
    #         "min": 0,
    #         "minColor": '#FFFFFF',
    #         "maxColor": '#003d99'

    #     }
    #     chart['legend'] = {
    #         "align": "right",
    #         "layout": "vertical",
    #         "margin": 0,
    #         "verticalAlign": 'top',
    #         "y": 25,
    #         "symbolHeight": 280
    #     }

    #     chart['plotOptions'] = {
    #         "heatmap": {
    #             "turboThreshold": len(data['series'])
    #         }
    #     }
    #     chart['yAxis']['title'] = {'text': self._(u'Ano de acesso aos documentos')}
    #     chart['xAxis']['title'] = {'text': self._(u'Ano de publicação de documentos')}

    #     return {'options': chart}

    def bibliometrics_cited_and_citing_years_heat(self, data):

        chart = self.highchart

        chart['chart']['type'] = 'heatmap'
        chart['xAxis'] = {'categories': data['categories_x']}
        chart['yAxis'] = {'categories': data['categories_y']}
        chart['series'] = [{'data': data['series']}]
        chart['colorAxis'] = {
            "min": 0,
            "minColor": '#FFFFFF',
            "maxColor": '#960D0D'

        }
        chart['legend'] = {
            "align": "right",
            "layout": "vertical",
            "margin": 0,
            "verticalAlign": 'top',
            "y": 25,
            "symbolHeight": 280
        }

        chart['plotOptions'] = {
            "heatmap": {
                "turboThreshold": len(data['series'])
            }
        }
        chart['yAxis']['title'] = {'text': self._(u'Ano de publicação de documentos do periódico. (citados)')}
        chart['xAxis']['title'] = {'text': self._(u'Ano de publicação dos documentos da Rede ScIELO. (citantes)')}

        return {'options': chart}

    def bibliometrics_jcr_average_impact_factor_percentile(self, data):

        chart = self.highchart

        chart['title'] = {'text': self._(u'Fator de impacto (Média de percentil)')}
        chart['xAxis'] = {'categories': data['categories']}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Média de percentil')}
        chart['plotOptions'] = {
            'line': {
                'dataLabels': {
                    'enabled': True
                }
            }
        }
        chart['tooltip'] = {
            'headerFormat': self._(u'Média de percentil'),
            'pointFormat': u'<br/><strong>'+self._(u'Ano base')+u'</strong>: {point.category}<br/><strong>{series.name}</strong>: {point.y}'
        }

        return {'options': chart}

    def bibliometrics_jcr_eigen_factor(self, data):

        chart = self.highchart

        chart['title'] = {'text': self._(u'Eigen Factor JCR')}
        chart['xAxis'] = {'categories': data['categories']}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Eigen Factor JCR')}
        chart['plotOptions'] = {
            'line': {
                'dataLabels': {
                    'enabled': True
                }
            }
        }
        chart['tooltip'] = {
            'headerFormat': self._(u'Eigen Factor JCR'),
            'pointFormat': u'<br/><strong>'+self._(u'Ano base')+u'</strong>: {point.category}<br/><strong>{series.name}</strong>: {point.y}'
        }

        return {'options': chart}

    def bibliometrics_jcr_received_citations(self, data):

        chart = self.highchart

        chart['title'] = {'text': self._(u'Received Citations JCR')}
        chart['xAxis'] = {'categories': data['categories']}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Received Citations JCR')}
        chart['plotOptions'] = {
            'line': {
                'dataLabels': {
                    'enabled': True
                }
            }
        }
        chart['tooltip'] = {
            'headerFormat': self._(u'Received Citations JCR'),
            'pointFormat': u'<br/><strong>'+self._(u'Ano base')+u'</strong>: {point.category}<br/><strong>{series.name}</strong>: {point.y}'
        }

        return {'options': chart}

    def bibliometrics_jcr_impact_factor(self, data):

        chart = self.highchart

        chart['title'] = {'text': self._(u'Fator de impacto JCR')}
        chart['xAxis'] = {'categories': data['categories']}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Fator de impacto JCR')}
        chart['plotOptions'] = {
            'line': {
                'dataLabels': {
                    'enabled': True
                }
            }
        }
        chart['tooltip'] = {
            'headerFormat': self._(u'Fator de impacto JCR'),
            'pointFormat': u'<br/><strong>'+self._(u'Ano base')+u'</strong>: {point.category}<br/><strong>{series.name}</strong>: {point.y}'
        }

        return {'options': chart}

    def usage_report(self, data):
        chart = self.highchart

        chart['credits'] = {'href': 'https://usage.apis.scielo.br','text': self._(u'Fonte: SciELO SUSHI API')}
        chart['title'] = {'text': self._(u'Total de acessos por ano e mês (API SUSHI)')}
        chart['series'] = data['series']
        chart['legend'] = {'enabled': True}
        chart['yAxis']['title'] = {'text': self._(u'Métricas')}
        chart['yAxis']['opposite'] = False
        chart['xAxis'] = {'type': 'datetime'}
        chart['rangeSelector'] = {'enabled': False}
        chart['tooltip'] = {
            'shared': True,
            'useHTML': True,
            'headerFormat': self._(u'Acessos em') + ' <strong>{point.x:%B %Y}</strong><table style="width: 100%; border-top: 1px solid #CCC;">',
            'pointFormat': u'<tr><td><span style="color:{point.color}">\u25CF</span> {series.name}: </td><td style="text-align: right"><strong>{point.y}</strong></td></tr>',
            'footerFormat': '</table>'
        }

        return {'options': chart}

    def bibliometrics_google_h5m5(self, data):

        chart = self.highchart

        chart['credits'] = {'href': 'http://scholar.google.com', 'text': self._(u'Fonte: Google Scholar')}
        chart['title'] = {'text': self._(u'Métricas H5M5')}
        chart['xAxis'] = {'categories': data['categories']}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Métricas H5M5')}
        chart['plotOptions'] = {
            'line': {
                'dataLabels': {
                    'enabled': True
                }
            }
        }
        chart['tooltip'] = {
            'headerFormat': self._(u'Métricas H5M5'),
            'pointFormat': u'<br/><strong>'+self._(u'Ano base')+u'</strong>: {point.category}<br/><strong>{series.name}</strong>: {point.y}',
            'followPointer': False,
        }

        return {'options': chart}

    def bibliometrics_impact_factor(self, data):

        name = {
            'impact_factor_0': self._(u'imediatez'),
            'impact_factor_1': self._(u'1 ano'),
            'impact_factor_2': self._(u'2 anos'),
            'impact_factor_3': self._(u'3 anos'),
            'impact_factor_4': self._(u'4 anos'),
            'impact_factor_5': self._(u'5 anos')
        }

        for i, serie in enumerate(data['series']):
            data['series'][i]['name'] = name[serie['name']]

        chart = self.highchart
        chart['title'] = {'text': self._(u'Impacto SciELO em 1, 2, 3, 4, 5 anos e Índice de Imediatez')}
        chart['xAxis'] = {'categories': data['categories']}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Impacto SciELO')}
        chart['tooltip'] = {
            'headerFormat': self._(u'Impacto SciELO'),
            'pointFormat': u'<br/><strong>'+self._(u'Ano base')+u'</strong>: {point.category}<br/><strong>{series.name}</strong>: {point.y}',
            'followPointer': True
        }

        return {'options': chart}

    def bibliometrics_journal_received_self_and_granted_citation_chart(self, data):

        name = {'self_citation': self._(u'Auto citação'), 'granted_citation': self._(u'Citações concedidas'), 'received_citation': self._(u'Citações recebidas')}

        for i, serie in enumerate(data['series']):
            data['series'][i]['name'] = name[serie['name']]

        chart = self.highchart
        chart['chart']['type'] = 'area'
        chart['title'] = {'text': self._(u'Distribuição de citações concedidas, recebidas e auto citações')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': None}
            }
        chart['legend'] = {'enabled': True}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de citações')}
        chart['yAxis']['opposite'] = False
        chart['tooltip'] = {
            'shared': True,
            'useHTML': True,
            'headerFormat': self._(u'Ano de publicação') + ' <strong>{point.key}</strong><table>',
            'pointFormat': u'<tr><td><span style="color:{point.color}">\u25CF</span> {series.name}: </td><td style="text-align: right"><strong>{point.y}</strong></td></tr>',
            'footerFormat': '</table>'
        }

        return {'options': chart}

    def publication_article_citable_documents(self, data):

        name = {'citable_documents': self._(u'Documentos citáveis'), 'not_citable_documents': self._(u'Documentos não citáveis')}

        for i, serie in enumerate(data['series']):
            data['series'][i]['name'] = name[serie['name']]

        chart = self.highchart
        chart['chart']['type'] = 'area'
        chart['title'] = {'text': self._(u'Distribuição de documentos citáveis e não citáveis')}
        chart['xAxis'] = {'title': {'text': self._(u'Ano de publicação')}}
        chart['legend'] = {'enabled': True}
        chart['series'] = data['series']
        chart['navigator'] = {
            'series': {
                'data': data['navigator_series']
            }
        }
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos')}
        chart['yAxis']['opposite'] = False
        chart['rangeSelector'] = {'enabled': False}
        chart['tooltip'] = {
            'shared': True,
            'useHTML': True,
            'headerFormat': self._(u'Ano de publicação') + ' <strong>{point.key}</strong><table>',
            'pointFormat': u'<tr><td><span style="color:{point.color}">\u25CF</span> {series.name}: </td><td style="text-align: right"><strong>{point.y}</strong></td><td style="text-align: right">&nbsp;({point.percentage:.2f}%)</td></tr>',
            'footerFormat': '</table>'
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
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos')}
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'%s documentos com %s referências bibliográficas' % ('<strong>{point.y}</strong>', '<strong>{point.category}</strong>'))
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
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos')}
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'%s documentos com %s autores' % ('<strong>{point.y}</strong>', '<strong>{point.category}</strong>'))
        }

        return {'options': chart}

    def publication_article_affiliations_map(self, data):

        chart = self.highchart
        del chart['chart']
        del chart['legend']
        del chart['yAxis']
        chart['title'] = {'text': self._(u'Distribuição de países de afiliação dos autores')}
        chart['legend'] = {
            'title': {
                'text': self._(u'Número de documentos')
            }
        }
        chart['colorAxis'] = {
            'min': 1,
            'max': sorted(data['series'][0]['data'])[-1],
            'type': 'logarithmic'
        }

        chart['mapNavigation'] = {
            'enabled': True,
            'buttonOptions': {
                'verticalAlign': 'bottom'
            }
        }
        chart['series'] = [{
            'data': [{'value': v, 'code': k, 'name': k} for k, v in dict(zip(data['categories'], data['series'][0]['data'])).items()],
            'joinBy': ['iso-a2', 'code'],
            'name': self._(u'Documentos'),
            'states': {
                'hover': {
                    'color': '#BADA55'
                }
            }
        }]
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span>' + self._(u'País de afiliação') + ' <strong>{point.name}</strong><br/>{series.name}: <strong>{point.value}</strong>'
        }

        return {'options': chart}

    def publication_article_affiliations(self, data):
        # convertendo ISO 3166 para texto
        country_names = [choices.ISO_3166.get(i, 'undefined') for i in data['categories']]
        data['categories'] = country_names

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de países de afiliação dos autores')}
        chart['xAxis'] = {
            'categories': data['categories'],
            'title': {'text': self._(u'País de afiliação')}
            }
        chart['plotOptions'] = {'series': {'colorByPoint': True}}
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos')}
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'País de afiliação') + ' <strong>{point.category}</strong><br>' + self._(u'Documentos') + ': <strong>{point.y}</strong>'
        }

        return {'options': chart}

    def publication_article_affiliations_by_publication_year(self, data):

        # convertendo ISO 3166 para texto
        for item in data['series']:
            item['name'] = choices.ISO_3166.get(item['name'].upper(), 'undefined')

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de países de afiliação dos autores por ano de publicação')}
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['navigator'] = {
            'series': {
                'data': data['navigator_series']
            }
        }
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos')}
        chart['yAxis']['opposite'] = False
        chart['xAxis'] = {'title': {'text': self._(u'Ano de publicação')}}
        chart['plotOptions'] = {
            'column': {'stacking': 'normal'}
        }
        chart['rangeSelector'] = {'enabled': False}
        chart['series'] = data['series']
        chart['tooltip'] = {
            'shared': False,
            'useHTML': True,
            'headerFormat': self._(u'Ano de publicação') + ' <strong>{point.x:%Y}</strong><table>',
            'pointFormat': u'<tr><td><span style="color:{point.color}">\u25CF</span> {series.name}: </td><td style="text-align: right"><strong>{point.y}</strong></td><td style="text-align: right">&nbsp;({point.percentage:.2f}%)</td></tr>',
            'footerFormat': '</table>'
        }

        return {'options': chart}

    def publication_article_year(self, data):

        data['categories'] = data['categories'][::-1]
        data['series'][0]['data'] = data['series'][0]['data'][::-1]

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de ano de publicação dos documentos')}
        chart['xAxis'] = {'title': {'text': self._(u'Ano de publicação')}}
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos')}
        chart['yAxis']['opposite'] = False
        chart['rangeSelector'] = {'enabled': False}
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Ano de publicação') + ' <strong>{point.category:%Y}</strong><br>' + self._(u'Documentos') + ': <strong>{point.y}</strong>'
        }

        return {'options': chart}

    def publication_article_languages(self, data):

        # convertendo ISO 639_1 para texto
        language_names = [choices.ISO_639_1.get(i.upper(), 'undefined') for i in data['categories']]
        data['categories'] = language_names

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
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos')}
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Idioma do documento') + ' <strong>{point.category}</strong><br>' + self._(u'Documentos') + ': <strong>{point.y}</strong>'
        }

        return {'options': chart}

    def publication_article_languages_by_publication_year(self, data):

        # convertendo ISO 639_1 para texto
        for item in data['series']:
            item['name'] = choices.ISO_639_1.get(item['name'].upper(), 'undefined')


        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de idiomas dos documentos por ano de publicação')}
        chart['legend'] = {'enabled': True}
        chart['series'] = data['series']
        chart['navigator'] = {
            'series': {
                'data': data['navigator_series']
            }
        }
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos')}
        chart['yAxis']['opposite'] = False
        chart['xAxis'] = {'title': {'text': self._(u'Ano de publicação')}}
        chart['plotOptions'] = {
            'column': {'stacking': 'normal'}
        }
        chart['rangeSelector'] = {'enabled': False}
        chart['series'] = data['series']
        chart['tooltip'] = {
            'shared': True,
            'useHTML': True,
            'headerFormat': self._(u'Ano de publicação') + ' <strong>{point.x:%Y}</strong><table>',
            'pointFormat': u'<tr><td><span style="color:{point.color}">\u25CF</span> {series.name}: </td><td style="text-align: right"><strong>{point.y}</strong></td><td style="text-align: right">&nbsp;({point.percentage:.2f}%)</td></tr>',
            'footerFormat': '</table>'
        }

        return {'options': chart}

    def publication_journal_year(self, data):

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de periódicos por ano de inclusão no SciELO')}
        chart['xAxis'] = {'title': {'text': self._(u'Ano de inclusão')}}
        chart['legend'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de periódicos')}
        chart['yAxis']['opposite'] = False
        chart['rangeSelector'] = {'enabled': False}
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Ano de inclusão') + ' <strong>{point.category:%Y}</strong><br>' + self._(u'Periódicos') + ': <strong>{point.y}</strong>'
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
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos')}
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Área temática') + ' <strong>{point.category}</strong><br>' + self._(u'Documentos') + ': <strong>{point.y}</strong>'
        }

        return {'options': chart}

    def publication_article_subject_areas_by_publication_year(self, data):

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de área temática dos documentos por ano de publicação')}
        chart['legend'] = {'enabled': True}
        chart['series'] = data['series']
        chart['navigator'] = {
            'series': {
                'data': data['navigator_series']
            }
        }
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos')}
        chart['yAxis']['opposite'] = False
        chart['xAxis'] = {'title': {'text': self._(u'Ano de publicação')}}
        chart['plotOptions'] = {
            'column': {'stacking': 'normal'}
        }
        chart['rangeSelector'] = {'enabled': False}
        chart['series'] = data['series']
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos')}
        chart['tooltip'] = {
            'shared': True,
            'useHTML': True,
            'headerFormat': self._(u'Ano de publicação') + ' <strong>{point.x:%Y}</strong><table>',
            'pointFormat': u'<tr><td><span style="color:{point.color}">\u25CF</span> {series.name}: </td><td style="text-align: right"><strong>{point.y}</strong></td><td style="text-align: right">&nbsp;({point.percentage:.2f}%)</td></tr>',
            'footerFormat': '</table>'
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
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos')}
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Tipo de documento') + ' <strong>{point.category}</strong><br>' + self._(u'Documentos') + ': <strong>{point.y}</strong>'
        }

        return {'options': chart}

    def publication_article_document_type_by_publication_year(self, data):
        # convertendo ISO 639_1 para texto

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de tipos de documentos por ano de publicação')}
        chart['legend'] = {'enabled': True}
        chart['series'] = data['series']
        chart['navigator'] = {
            'series': {
                'data': data['navigator_series']
            }
        }
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos')}
        chart['yAxis']['opposite'] = False
        chart['xAxis'] = {'title': {'text': self._(u'Ano de publicação')}}
        chart['plotOptions'] = {
            'column': {'stacking': 'normal'}
        }
        chart['rangeSelector'] = {'enabled': False}
        chart['series'] = data['series']
        chart['tooltip'] = {
            'shared': True,
            'useHTML': True,
            'headerFormat': self._(u'Ano de publicação') + ' <strong>{point.x:%Y}</strong><table>',
            'pointFormat': u'<tr><td><span style="color:{point.color}">\u25CF</span> {series.name}: </td><td style="text-align: right"><strong>{point.y}</strong></td><td style="text-align: right">&nbsp;({point.percentage:.2f}%)</td></tr>',
            'footerFormat': '</table>'
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
        chart['yAxis']['title'] = {'text': self._(u'Número de periódicos')}
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Situação da publicação') + ' <strong>{point.category}</strong><br>' + self._(u'Periódicos') + ': <strong>{point.y}</strong>'
        }

        return {'options': chart}

    def publication_article_licenses_by_publication_year(self, data):

        chart = self.highchart
        chart['chart']['type'] = 'column'
        chart['title'] = {'text': self._(u'Distribuição de licenças de uso por ano de publicação')}
        chart['legend'] = {'enabled': True}
        chart['series'] = data['series']
        chart['navigator'] = {
            'series': {
                'data': data['navigator_series']
            }
        }
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos')}
        chart['yAxis']['opposite'] = False
        chart['xAxis'] = {'title': {'text': self._(u'Ano de publicação')}}
        chart['plotOptions'] = {
            'column': {'stacking': 'normal'}
        }
        chart['rangeSelector'] = {'enabled': False}
        chart['tooltip'] = {
            'shared': True,
            'useHTML': True,
            'headerFormat': self._(u'Ano de publicação') + ' <strong>{point.x:%Y}</strong><table>',
            'pointFormat': u'<tr><td><span style="color:{point.color}">\u25CF</span> {series.name}: </td><td style="text-align: right"><strong>{point.y}</strong></td><td style="text-align: right">&nbsp;({point.percentage:.2f}%)</td></tr>',
            'footerFormat': '</table>'
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
        chart['yAxis']['title'] = {'text': self._(u'Número de documentos')}
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Licença') + ' <strong>{point.category}</strong><br>' + self._(u'Documentos') + ': <strong>{point.y}</strong>'
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
        chart['yAxis']['title'] = {'text': self._(u'Número de periódicos')}
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
        chart['yAxis']['title'] = {'text': self._(u'Número de periódicos')}
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Licença') + ' <strong>{point.category}</strong><br>' + self._(u'Periódicos') + ': <strong>{point.y}</strong>'
        }

        return {'options': chart}

    def bymonthandyear(self, data):

        chart = self.highchart
        chart['title'] = {'text': self._(u'Total de acessos por ano e mês')}
        chart['series'] = data['series']
        chart['navigator'] = {
            'series': {
                'data': data['navigator_series']
            }
        }
        chart['legend'] = {'enabled': True}
        chart['yAxis']['title'] = {'text': self._(u'Acessos')}
        chart['yAxis']['opposite'] = False
        chart['rangeSelector'] = {'enabled': False}
        chart['tooltip'] = {
            'shared': True,
            'useHTML': True,
            'headerFormat': self._(u'Acessos em') + ' <strong>{point.x:%B %Y}</strong><table style="width: 100%; border-top: 1px solid #CCC;">',
            'pointFormat': u'<tr><td><span style="color:{point.color}">\u25CF</span> {series.name}: </td><td style="text-align: right"><strong>{point.y}</strong></td></tr>',
            'footerFormat': '</table>'
        }

        return {'options': chart}

    def documenttype(self, data):

        chart = self.highchart
        chart['chart']['type'] = 'pie'
        chart['title'] = {'text': self._('Total de accessos por tipo de documento')}
        chart['series'] = data['series']
        chart['tooltip'] = {
            'headerFormat': '',
            'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'%s acessos a documentos do tipo %s' % ('<strong>{point.y}</strong> ({point.percentage:.0f}%)', '<strong>{point.name}</strong>'))
        }

        return {'options': chart}

    def lifetime(self, data):

        charts = []
        for item in data:
            chart = self.highchart
            chart['chart']['type'] = 'column'
            chart['legend'] = {'enabled': False}
            chart['title'] = {'text': self._(u'Vida útil de artigos por número de acessos em') + ' ' + item['series'][0]['name']}
            chart['series'] = item['series']
            chart['yAxis']['title'] = {'text': self._(u'Acessos') + u' ' + item['series'][0]['name']}
            chart['yAxis']['opposite'] = False
            chart['rangeSelector'] = {'enabled': False}
            chart['xAxis'] = {'title': {'text': self._(u'Ano de publicação')}}
            chart['tooltip'] = {
                'shared': True,
                'headerFormat': '',
                'pointFormat': u'<span style="color:{point.color}">\u25CF</span> ' + self._(u'Ano de referência') + ' <strong>{series.name}</strong><br>' + self._(u'%s acessos aos documentos do ano %s' % ('<strong>{point.y}</strong>', '<strong>{point.category:%Y}</strong>'))
            }
            charts.append(chart)

        return charts
