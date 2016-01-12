from pyramid.session import SignedCookieSessionFactory
from pyramid.renderers import JSONP
from pyramid.config import Configurator
from pyramid.settings import aslist, asbool

from analytics import controller
from analytics import charts_config
from thrift_clients import clients

from analytics.views_website import cache_region as views_website_cache_region
from analytics.controller import cache_region as controller_cache_region

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_renderer('jsonp', JSONP(param_name='callback', indent=4))

    def add_stats(request):
        return controller.Stats(
            settings['articlemeta'],
            settings['publicationstats'],
            settings['accessstats'],
            settings['citedby']
        )

    def add_chartsconfig(request):
        return charts_config.chartsconfig(request)

    config.include('pyramid_mako')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index_web', '/')
    config.add_route('faq_web', '/w/faq')
    config.add_route('downloads', '/w/downloads')
    config.add_route('accesses_web', '/w/accesses')
    config.add_route('accesses_list_journals_web', '/w/accesses/list/journals')
    config.add_route('accesses_list_issues_web', '/w/accesses/list/issues')
    config.add_route('accesses_list_articles_web', '/w/accesses/list/articles')
    config.add_route('accesses_bydocumenttype', '/ajx/accesses/bydocumenttype')
    config.add_route('accesses_bymonthandyear', '/ajx/accesses/bymonthandyear')
    config.add_route('accesses_lifetime', '/ajx/accesses/lifetime')
    config.add_route('publication_size_web', '/w/publication/size')
    config.add_route('publication_journal_web', '/w/publication/journal')
    config.add_route('publication_size', '/ajx/publication/size')
    config.add_route('publication_journal_year', '/ajx/publication/journal/year')
    config.add_route('publication_journal_licenses', '/ajx/publication/journal/licenses')
    config.add_route('publication_journal_subject_areas', '/ajx/publication/journal/subject_areas')
    config.add_route('publication_journal_status', '/ajx/publication/journal/status')
    config.add_route('publication_article_citable_documents', '/ajx/publication/citabledocuments')
    config.add_route('publication_article_web', '/w/publication/article')
    config.add_route('publication_article_licenses', '/ajx/publication/article/licenses')
    config.add_route('publication_article_licenses_publication_year', '/ajx/publication/article/licenses_publication_year')
    config.add_route('publication_article_document_type', '/ajx/publication/article/document_type')
    config.add_route('publication_article_references', '/ajx/publication/article/references')
    config.add_route('publication_article_languages', '/ajx/publication/article/languages')
    config.add_route('publication_article_authors', '/ajx/publication/article/authors')
    config.add_route('publication_article_affiliations', '/ajx/publication/article/affiliations')
    config.add_route('publication_article_year', '/ajx/publication/article/year')
    config.add_route('publication_article_subject_areas', '/ajx/publication/article/subject_areas')
    config.add_route('bibliometrics_journal_web', '/w/bibliometrics/journal')
    config.add_route('bibliometrics_list_granted_web', '/bibliometrics/list/granted')
    config.add_route('bibliometrics_list_received_web', '/bibliometrics/list/received')
    config.add_route('bibliometrics_list_citing_forms_web', '/bibliometrics/list/citing_forms')   
    config.add_route('bibliometrics_list_impact_factor_web', '/bibliometrics/list/impact_factor')   
    config.add_route('bibliometrics_journal_received_self_and_granted_citation_chart', '/ajx/bibliometrics/journal/received_self_and_granted_citation_chart')
    config.add_route('bibliometrics_journal_impact_factor_chart', '/ajx/bibliometrics/journal/impact_factor_chart')
    config.add_request_method(add_stats, 'stats', reify=True)
    config.add_request_method(add_chartsconfig, 'chartsconfig', reify=True)

    config.add_subscriber('analytics.subscribers.add_renderer_globals',
                          'pyramid.events.BeforeRender')
    config.add_subscriber('analytics.subscribers.add_localizer',
                          'pyramid.events.NewRequest')
    config.add_translation_dirs('analytics:locale')

    ## Cache Settings Config
    if 'memcached_host' in settings:
        cache_config = {}
        cache_config['expiration_time'] = int(settings.get('memcached_expiration_time', 2592000)) # a month cache
        cache_config['arguments'] = {'url': settings['memcached_host'], 'binary': True}
        views_website_cache_region.configure('dogpile.cache.pylibmc', **cache_config)
        controller_cache_region.configure('dogpile.cache.pylibmc', **cache_config)
    else:
        views_website_cache_region.configure('dogpile.cache.null')
        controller_cache_region.configure('dogpile.cache.null')

    ## Session config
    navegation_session_factory = SignedCookieSessionFactory('sses_navegation')
    config.set_session_factory(navegation_session_factory)

    config.scan()

    return config.make_wsgi_app()
