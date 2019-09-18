#coding: utf-8
import requests
from datetime import datetime

from pyramid.view import view_config
from dogpile.cache import make_region
from citedby.custom_query import journal_titles
from scielojcr import jcrindicators

from analytics.control_manager import base_data_manager

cache_region = make_region(name='views_website_cache')


@view_config(route_name='bibliometrics_journal_web', renderer='templates/website/bibliometrics_journal.mako')
@base_data_manager
def bibliometrics_journal(request):

    data = request.data_manager
    data['page'] = 'bibliometrics'
    titles = request.GET.get('titles', None)

    titles = titles.split('||') if titles else []

    if data['selected_journal_code']:
        journal = request.stats.articlemeta.journal(code=data['selected_journal_code'])
        titles.append(journal.title)
        titles.append(journal.abbreviated_title)
        titles.extend(x['title'] for x in journal_titles.load(data['selected_journal_code']).get('should', []) if x['title'] not in titles)

    data['titles'] = []
    if titles and not len(titles) == 0:
        forms = set([i.strip() for i in titles if i])
        data['titles'] = u'||'.join(forms)

    return data


@view_config(route_name='bibliometrics_journal_jcr', renderer='templates/website/bibliometrics_journal_jcr.mako')
@base_data_manager
def bibliometrics_journal_jcr(request):

    data = request.data_manager
    data['page'] = 'bibliometrics'

    jcrind = request.stats.bibliometrics.jcr(issn=data['selected_journal_code'])

    data['jcr'] = jcrind
    data['jct_extraction_date'] = datetime.strptime(jcrindicators.UPDATE_INDICATORS, '%Y-%m-%d')

    return data

@view_config(route_name='bibliometrics_journal_altmetric', renderer='templates/website/bibliometrics_journal_altmetric.mako')
@base_data_manager
def bibliometrics_journal_altmetric(request):

    data = request.data_manager
    data['page'] = 'bibliometrics'

    altmetric = request.stats.bibliometrics.altmetric(issn=data['selected_journal_code'])

    data['altmetric'] = altmetric

    return data

@view_config(route_name='bibliometrics_journal_cited_and_citing_years_heat_web', renderer='templates/website/bibliometrics_journal_received_citations_heat.mako')
@base_data_manager
def bibliometrics_journal_cited_and_citing_years_heat_web(request):
    data = request.data_manager
    data['page'] = 'bibliometrics'
    titles = request.GET.get('titles', None)
    citing_year = request.GET.get('citing_year', None)
    cited_year = request.GET.get('cited_year', None)

    titles = titles.split('||') if titles else []

    if data['selected_journal_code']:
        journal = request.stats.articlemeta.journal(code=data['selected_journal_code'])
        titles.append(journal.title)
        titles.append(journal.abbreviated_title)
        titles.extend(x['title'] for x in journal_titles.load(data['selected_journal_code']).get('should', []) if x['title'] not in titles)

    data['blist'] = {}
    data['titles'] = []
    if titles and not len(titles) == 0:
        forms = set([i.strip() for i in titles if i])
        data['titles'] = u'||'.join(forms)

    data['citing_list'] = []
    if citing_year and cited_year:
        citing_list = request.stats.bibliometrics.cited_and_citing_years_document_list(
            data['selected_journal_code'],
            titles,
            citing_year=citing_year,
            cited_year=cited_year
        )

        data['citing_list'] = citing_list.get('citing_list', 0)

    return data

@view_config(route_name='bibliometrics_list_impact_factor_web', renderer='templates/website/bibliometrics_list_impact_factor.mako')
@base_data_manager
def bibliometrics_list_impact_factor(request):
    data = request.data_manager
    data['page'] = 'bibliometrics'
    titles = request.GET.get('titles', None)

    titles = titles.split('||') if titles else []

    if data['selected_journal_code']:
        journal = request.stats.articlemeta.journal(code=data['selected_journal_code'])
        titles.append(journal.title)
        titles.append(journal.abbreviated_title)
        titles.extend(x['title'] for x in journal_titles.load(data['selected_journal_code']).get('should', []) if x['title'] not in titles)

    data['blist'] = {}
    data['titles'] = []
    if titles and not len(titles) == 0:
        forms = set([i.strip() for i in titles if i])
        data['blist'] = request.stats.impact_factor(data['selected_journal_code'], journal.collection_acronym, titles)
        data['titles'] = u'||'.join(forms)

    return data


@view_config(route_name='bibliometrics_list_citing_half_life_web', renderer='templates/website/bibliometrics_list_citing_half_life.mako')
@base_data_manager
def bibliometrics_list_citing_half_life(request):
    data = request.data_manager
    data['page'] = 'bibliometrics'
    titles = request.GET.get('titles', None)

    titles = titles.split('||') if titles else []

    if data['selected_journal_code']:
        journal = request.stats.articlemeta.journal(code=data['selected_journal_code'])
        titles.append(journal.title)
        titles.append(journal.abbreviated_title)
        titles.extend(x['title'] for x in journal_titles.load(data['selected_journal_code']).get('should', []) if x['title'] not in titles)

    data['blist'] = {}
    data['titles'] = []
    if titles and not len(titles) == 0:
        forms = set([i.strip() for i in titles if i])
        data['blist'] = request.stats.citing_half_life(data['selected_journal_code'], journal.collection_acronym, titles)
        data['titles'] = u'||'.join(forms)

    return data


@view_config(route_name='bibliometrics_list_general_indicators_web', renderer='templates/website/bibliometrics_list_general_indicators.mako')
@base_data_manager
def bibliometrics_list_general_indicators(request):
    data = request.data_manager
    data['page'] = 'bibliometrics'

    return data


@view_config(route_name='bibliometrics_list_citing_forms_web', renderer='templates/website/bibliometrics_list_citing_forms.mako')
@base_data_manager
def bibliometrics_list_citing_forms(request):
    data = request.data_manager
    data['page'] = 'bibliometrics'
    titles = request.GET.get('titles', None)

    titles = titles.split('||') if titles else []

    if data['selected_journal_code']:
        journal = request.stats.articlemeta.journal(code=data['selected_journal_code'])
        titles.append(journal.title)
        titles.append(journal.abbreviated_title)
        titles.extend(x['title'] for x in journal_titles.load(data['selected_journal_code']).get('should', []) if x['title'] not in titles)

    data['blist'] = []
    data['titles'] = []
    if titles and not len(titles) == 0:
        forms = set([i.strip() for i in titles if i])
        data['blist'] = request.stats.bibliometrics.citing_forms(data['selected_journal_code'], forms, py_range=data['py_range'])
        data['titles'] = u'||'.join(forms)

    return data


@view_config(route_name='bibliometrics_list_received_web', renderer='templates/website/bibliometrics_list_received.mako')
@base_data_manager
def bibliometrics_list_received(request):
    data = request.data_manager
    data['page'] = 'bibliometrics'
    titles = request.GET.get('titles', None)

    titles = titles.split('||') if titles else []

    if data['selected_journal_code']:
        journal = request.stats.articlemeta.journal(code=data['selected_journal_code'])
        titles.append(journal.title)
        titles.append(journal.abbreviated_title)
        titles.extend(x['title'] for x in journal_titles.load(data['selected_journal_code']).get('should', []) if x['title'] not in titles)

    data['blist'] = []
    data['titles'] = []
    if titles and not len(titles) == 0:
        forms = set([i.strip() for i in titles if i])
        data['blist'] = request.stats.bibliometrics.received_citations(data['selected_journal_code'], forms, py_range=data['py_range'])
        data['titles'] = u'||'.join(forms)

    return data


@view_config(route_name='bibliometrics_list_granted_web', renderer='templates/website/bibliometrics_list_granted.mako')
@base_data_manager
def bibliometrics_list_granted(request):
    data = request.data_manager
    data['page'] = 'bibliometrics'

    data['blist'] = []
    if data['selected_journal_code']:
        data['blist'] = request.stats.bibliometrics.granted_citations(
            data['selected_journal_code'],
            py_range=data['py_range'])

    return data

@view_config(route_name='bibliometrics_document_list_received_citations', renderer='templates/website/bibliometrics_document_list_received_citations.mako')
@base_data_manager
def bibliometrics_document_list_received_citations(request):
    data = request.data_manager
    data['page'] = 'bibliometrics'
    data['citedby'] = request.stats.bibliometrics.document_received_citations(
        request.data_manager.get('selected_document_code', 0))

    return data


@view_config(route_name='index_web', renderer='templates/website/home.mako')
@base_data_manager
def index(request):
    data = request.data_manager
    data['page'] = 'home'

    data['h5m5'] = request.stats.bibliometrics.google_h5m5(data['selected_journal_code'])

    titles = request.GET.get('titles', None)

    titles = titles.split('||') if titles else []

    if data['selected_journal_code']:
        journal = request.stats.articlemeta.journal(code=data['selected_journal_code'])
        titles.append(journal.title)
        titles.append(journal.abbreviated_title)
        titles.extend(x['title'] for x in journal_titles.load(data['selected_journal_code']).get('should', []) if x['title'] not in titles)

    data['titles'] = []
    if titles and not len(titles) == 0:
        forms = set([i.strip() for i in titles if i])
        data['titles'] = u'||'.join(forms)

    return data


@view_config(route_name='faq_web', renderer='templates/website/faq.mako')
@base_data_manager
def faq(request):

    data = request.data_manager
    data['page'] = 'faq'

    return data


@view_config(route_name='reports', renderer='templates/website/reports.mako')
@base_data_manager
def reports(request):
    from decimal import Decimal

    data = request.data_manager
    data['page'] = 'reports'

    tabsurl = 'https://static.scielo.org/tabs/tabs_network.zip'
    rd = requests.head(tabsurl).headers
    contentlength = Decimal(rd.get('content-length', 0))/Decimal(1024000)
    data['tabs'] = [
        {
            'collection': {'name': 'Network'},
            'tabsurl': tabsurl,
            'tabsfilename': 'tabs_network.zip',
            'contentlength': '%.2f' % contentlength,
            'lastmodified': rd.get('last-modified', 'undefined'),
            'is_available': True if contentlength > Decimal(0.001) else False
        }
    ]

    for collection in data['collections']:
        coll_code = 'bra' if collection == 'scl' else collection
        tabsfilename = 'tabs_%s.zip' % coll_code
        tabsurl = 'https://static.scielo.org/tabs/%s' % tabsfilename
        rd = requests.head(tabsurl).headers
        contentlength = Decimal(rd.get('content-length', 0))/Decimal(1024000)
        lastmodified = rd.get('last-modified', 'undefined')
        data['tabs'].append({
            'collection': data['collections'][collection],
            'tabsurl': tabsurl,
            'tabsfilename': tabsfilename,
            'contentlength': '%.2f' % contentlength,
            'lastmodified': lastmodified,
            'is_available': True if contentlength > Decimal(0.001) else False
        })

    return data


@view_config(route_name='accesses_list_journals_web', renderer='templates/website/access_list_journals.mako')
@base_data_manager
def accesses_list_journals(request):

    data = request.data_manager
    data['page'] = 'accesses'

    data['aclist'] = request.stats.access.list_journals(
        data['selected_code'],
        data['selected_collection_code'],
        data['py_range'],
        data['sa_scope'],
        data['la_scope'],
        data['range_start'],
        data['range_end']
    )

    return data


@view_config(route_name='accesses_list_issues_web', renderer='templates/website/access_list_issues.mako')
@base_data_manager
def accesses_list_issues(request):

    data = request.data_manager
    data['page'] = 'accesses'

    data['aclist'] = request.stats.access.list_issues(
        data['selected_code'],
        data['selected_collection_code'],
        data['py_range'],
        data['sa_scope'],
        data['la_scope'],
        data['range_start'],
        data['range_end']
    )

    return data


@view_config(route_name='accesses_list_articles_web', renderer='templates/website/access_list_articles.mako')
@base_data_manager
def accesses_list_articles(request):

    data = request.data_manager
    data['page'] = 'accesses'

    data['aclist'] = request.stats.access.list_articles(
        data['selected_code'],
        data['selected_collection_code'],
        data['py_range'],
        data['sa_scope'],
        data['la_scope'],
        data['range_start'],
        data['range_end']
    )

    return data


@view_config(route_name='accesses_web', renderer='templates/website/accesses.mako')
@base_data_manager
def accesses(request):

    data = request.data_manager
    data['page'] = 'accesses'

    return data

@view_config(route_name='accesses_document_web', renderer='templates/website/accesses_document.mako')
@base_data_manager
def accesses_document(request):

    data = request.data_manager
    data['page'] = 'accesses'

    return data

@view_config(route_name='publication_size_web', renderer='templates/website/publication_size.mako')
@base_data_manager
def publication_size(request):

    data = request.data_manager
    data['page'] = 'publication'

    return data


@view_config(route_name='publication_journal_web', renderer='templates/website/publication_journal.mako')
@base_data_manager
def publication_journal(request):

    data = request.data_manager
    data['page'] = 'publication'

    return data


@view_config(route_name='publication_article_web', renderer='templates/website/publication_article.mako')
@base_data_manager
def publication_article(request):

    data = request.data_manager
    data['page'] = 'publication'

    return data


@view_config(route_name='publication_article_web_by_publication_year', renderer='templates/website/publication_article_by_publication_year.mako')
@base_data_manager
def publication_article_by_publication_year(request):

    data = request.data_manager
    data['page'] = 'publication'

    return data
