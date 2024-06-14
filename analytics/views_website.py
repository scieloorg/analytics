#coding: utf-8
import requests
from datetime import datetime, timedelta

from pyramid.view import view_config
from dogpile.cache import make_region
from citedby.custom_query import journal_titles
# from scielojcr import jcrindicators

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


# @view_config(route_name='bibliometrics_journal_jcr', renderer='templates/website/bibliometrics_journal_jcr.mako')
# @base_data_manager
# def bibliometrics_journal_jcr(request):

#     data = request.data_manager
#     data['page'] = 'bibliometrics'

#     jcrind = request.stats.bibliometrics.jcr(issn=data['selected_journal_code'])

#     data['jcr'] = jcrind
#     data['jct_extraction_date'] = datetime.strptime(jcrindicators.UPDATE_INDICATORS, '%Y-%m-%d')

#     return data


@view_config(route_name='bibliometrics_journal_altmetric', renderer='templates/website/bibliometrics_journal_altmetric.mako')
@base_data_manager
def bibliometrics_journal_altmetric(request):

    data = request.data_manager
    data['page'] = 'bibliometrics'

    altmetric = request.stats.bibliometrics.altmetric(issn=data['selected_journal_code'])

    data['altmetric'] = altmetric

    return data


@view_config(route_name='bibliometrics_list_general_indicators_web', renderer='templates/website/bibliometrics_list_general_indicators.mako')
@base_data_manager
def bibliometrics_list_general_indicators(request):
    data = request.data_manager
    data['page'] = 'bibliometrics'

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


@view_config(route_name='accesses_web', renderer='templates/website/accesses.mako')
@base_data_manager
def accesses(request):

    data = request.data_manager
    data['page'] = 'accesses'

    return data


@view_config(route_name='accesses_list_journals_web', renderer='templates/website/accesses_list_journals.mako')
@base_data_manager
def accesses_list_journals(request):

    data = request.data_manager
    data['page'] = 'accesses'

    data['usage'] = request.stats.usage.get_usage_report(
        issn=data['selected_code'] if len(data['selected_code']) >= 8 else '',
        collection=data['selected_collection_code'],
        begin_date=data['range_start'],
        end_date=data['range_end'],
        granularity='totals',
        report_code='tr_j1',
        target='table',
    )

    return data


@view_config(route_name='accesses_list_journals_language', renderer='templates/website/accesses_list_journals_language.mako')
@base_data_manager
def accesses_list_journals_language(request):

    data = request.data_manager
    data['page'] = 'accesses'

    data['usage'] = request.stats.usage.get_usage_report(
        issn=data['selected_code'] if len(data['selected_code']) >= 8 else '',
        collection=data['selected_collection_code'],
        begin_date=data['range_start'],
        end_date=data['range_end'],
        granularity='totals',
        report_code='lr_j1',
        target='table',
    )

    return data

@view_config(route_name='accesses_journal_usage_data_web', renderer='templates/website/accesses_journal_usage_data.mako')
@base_data_manager
def accesses_journal_usage_data_web(request):
    data = request.data_manager
    data['page'] = 'accesses_journal_usage_data'

    return data


@view_config(route_name='bibliometrics_journal_citation_data_web', renderer='templates/website/bibliometrics_journal_citation_data.mako')
@base_data_manager
def bibliometrics_journal_citation_data_web(request):
    data = request.data_manager
    data['page'] = 'bibliometrics_journal_citation_data'

    last_year = (datetime.now() - timedelta(days=365)).strftime('%Y')
    selected_year = request.GET.get('selected_year', '')
    data['selected_year'] = selected_year if selected_year.isdigit() else last_year

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
