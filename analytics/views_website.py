#coding: utf-8
import requests

from pyramid.view import view_config

from dogpile.cache import make_region

from analytics.control_manager import base_data_manager
from analytics.custom_queries import custom_query

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
        titles.extend(x['title'] for x in custom_query.load(data['selected_journal_code']).get('should', []) if x['title'] not in titles)

    data['titles'] = []
    if titles and not len(titles) == 0:
        forms = set([i.strip() for i in titles if i])
        data['titles'] = u'||'.join(forms)

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
        titles.extend(x['title'] for x in custom_query.load(data['selected_journal_code']).get('should', []) if x['title'] not in titles)

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
        titles.extend(x['title'] for x in custom_query.load(data['selected_journal_code']).get('should', []) if x['title'] not in titles)

    data['blist'] = {}
    data['titles'] = []
    if titles and not len(titles) == 0:
        forms = set([i.strip() for i in titles if i])
        data['blist'] = request.stats.citing_half_life(data['selected_journal_code'], journal.collection_acronym, titles)
        data['titles'] = u'||'.join(forms)

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
        titles.extend(x['title'] for x in custom_query.load(data['selected_journal_code']).get('should', []) if x['title'] not in titles)

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
        titles.extend(x['title'] for x in custom_query.load(data['selected_journal_code']).get('should', []) if x['title'] not in titles)

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


@view_config(route_name='index_web', renderer='templates/website/home.mako')
@base_data_manager
def index(request):
    data = request.data_manager
    data['page'] = 'home'

    data['h5m5'] = request.stats.bibliometrics.google_h5m5(data['selected_journal_code'])

    return data


@view_config(route_name='faq_web', renderer='templates/website/faq.mako')
@base_data_manager
def faq(request):

    data = request.data_manager
    data['page'] = 'faq'

    return data


@view_config(route_name='downloads', renderer='templates/website/downloads.mako')
@base_data_manager
def downloads(request):
    from decimal import Decimal

    data = request.data_manager
    data['page'] = 'downloads'

    data['tabs'] = []

    for collection in data['collections']:
        coll_code = 'bra' if collection == 'scl' else collection
        tabsfilename = 'tabs_%s.zip' % coll_code
        tabsurl = 'http://static.scielo.org/tabs/%s' % tabsfilename
        rd = requests.head(tabsurl)
        rd = rd.headers
        contentlength = Decimal(rd.get('content-length', 0))/Decimal(1024000)
        lastmodified = rd.get('last-modified', 'undefined')
        data['tabs'].append({
            'collection': data['collections'][collection],
            'tabsurl': tabsurl,
            'tabsfilename': tabsfilename,
            'contentlength': contentlength,
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
