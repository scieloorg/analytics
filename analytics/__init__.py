import os
from pyramid.session import SignedCookieSessionFactory
from pyramid.renderers import JSONP
from pyramid.config import Configurator

from analytics import controller
from analytics import charts_config

from analytics.views_website import cache_region as views_website_cache_region
from analytics.views_ajax import cache_region as views_ajax_cache_region
from analytics.controller import cache_region as controller_cache_region
from analytics.control_manager import cache_region as control_manager_cache_region


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_renderer('jsonp', JSONP(param_name='callback', indent=4))

    def add_stats(request):
        return controller.Stats(
            settings.get('articlemeta', None),
            settings.get('publicationstats', None),
            settings.get('citedby', None),
            settings.get('usage', None),
        )

    def add_chartsconfig(request):
        return charts_config.chartsconfig(request)

    config.include('pyramid_mako')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index_web', '/')
    config.add_route('faq_web', '/w/faq')
    config.add_route('reports', '/w/reports')
    config.add_route('usage_report_chart', '/ajx/usage/usage_report_chart')
    config.add_route('accesses_web', '/w/accesses')
    config.add_route('accesses_list_journals_web', '/w/accesses/list/journals')
    config.add_route('accesses_list_journals_language', '/w/accesses/list/journals/language')
    config.add_route('accesses_list_journals_top100_articles', '/w/accesses/list/journals/top100_articles')
    config.add_route('accesses_journal_usage_data_web', '/w/accesses/journal/usage_data')
    config.add_route('publication_size_web', '/w/publication/size')
    config.add_route('publication_size', '/ajx/publication/size')
    config.add_route('publication_journal_web', '/w/publication/journal')
    config.add_route('publication_journal_year', '/ajx/publication/journal/year')
    config.add_route('publication_journal_licenses', '/ajx/publication/journal/licenses')
    config.add_route('publication_journal_subject_areas', '/ajx/publication/journal/subject_areas')
    config.add_route('publication_journal_status', '/ajx/publication/journal/status')
    config.add_route('publication_journal_status_detailde', '/ajx/publication/journal/status_detailde')
    config.add_route('publication_article_citable_documents', '/ajx/publication/citabledocuments')
    config.add_route('publication_article_web', '/w/publication/article')
    config.add_route('publication_article_web_by_publication_year', '/w/publication/article_by_publication_year')
    config.add_route('publication_article_licenses', '/ajx/publication/article/licenses')
    config.add_route('publication_article_licenses_publication_year', '/ajx/publication/article/licenses_publication_year')
    config.add_route('publication_article_document_type', '/ajx/publication/article/document_type')
    config.add_route('publication_article_document_type_publication_year', '/ajx/publication/article/document_type_publication_year')
    config.add_route('publication_article_references', '/ajx/publication/article/references')
    config.add_route('publication_article_languages', '/ajx/publication/article/languages')
    config.add_route('publication_article_languages_publication_year', '/ajx/publication/article/languages_publication_year')
    config.add_route('publication_article_authors', '/ajx/publication/article/authors')
    config.add_route('publication_article_affiliations', '/ajx/publication/article/affiliations')
    config.add_route('publication_article_affiliations_map', '/ajx/publication/article/affiliations_map')
    config.add_route('publication_article_affiliations_publication_year', '/ajx/publication/article/affiliations_publication_year')
    config.add_route('publication_article_year', '/ajx/publication/article/year')
    config.add_route('publication_article_subject_areas', '/ajx/publication/article/subject_areas')
    config.add_route('publication_article_subject_areas_publication_year', '/ajx/publication/article/subject_areas_publication_year')
    config.add_route('bibliometrics_journal_web', '/w/bibliometrics/journal')
    # config.add_route('bibliometrics_journal_jcr', '/w/bibliometrics/journal/jcr')
    config.add_route('bibliometrics_journal_altmetric', '/w/bibliometrics/journal/altmetric')
    config.add_route('bibliometrics_list_general_indicators_web', '/w/bibliometrics/list/general_indicators')
    config.add_route('bibliometrics_journal_citation_data_web', '/w/bibliometrics/journal/citation_data')
    config.add_route('bibliometrics_journal_google_h5m5_chart', '/ajx/bibliometrics/journal/google_h5m5_chart')
    # config.add_route('bibliometrics_journal_jcr_impact_factor_chart', '/ajx/bibliometrics/journal/jcr_impact_factor_chart')
    # config.add_route('bibliometrics_journal_jcr_received_citations_chart', '/ajx/bibliometrics/journal/jcr_received_citations_chart')
    # config.add_route('bibliometrics_journal_jcr_eigen_factor_chart', '/ajx/bibliometrics/journal/jcr_eigen_factor_chart')
    # config.add_route('bibliometrics_journal_jcr_average_impact_factor_percentile_chart', '/ajx/bibliometrics/journal/jcr_average_impact_factor_percentile_chart')
    config.add_request_method(add_stats, 'stats', reify=True)
    config.add_request_method(add_chartsconfig, 'chartsconfig', reify=True)

    config.add_subscriber('analytics.subscribers.add_renderer_globals',
                          'pyramid.events.BeforeRender')
    config.add_subscriber('analytics.subscribers.add_localizer',
                          'pyramid.events.NewRequest')
    config.add_translation_dirs('analytics:locale')

    # Cache Settings Config
    memcached_host = (
        os.environ.get(
            'MEMCACHED_HOST',
            settings.get('memcached_host', None)
        )
    )

    memcached_expiration_time = int((
        os.environ.get(
            'MEMCACHED_EXPIRATION_TIME',
            settings.get('memcached_expiration_time', 2592000)
        )
    ))

    if memcached_host:
        cache_config = {}
        cache_config['expiration_time'] = int(memcached_expiration_time)  # a month cache
        cache_config['arguments'] = {'url': memcached_host, 'binary': True}
        views_ajax_cache_region.configure('dogpile.cache.pylibmc', **cache_config)
        views_website_cache_region.configure('dogpile.cache.pylibmc', **cache_config)
        controller_cache_region.configure('dogpile.cache.pylibmc', **cache_config)
        control_manager_cache_region.configure('dogpile.cache.pylibmc', **cache_config)
    else:
        views_website_cache_region.configure('dogpile.cache.null')
        controller_cache_region.configure('dogpile.cache.null')
        control_manager_cache_region.configure('dogpile.cache.null')
        views_ajax_cache_region.configure('dogpile.cache.null')

    # Session config
    navegation_session_factory = SignedCookieSessionFactory('sses_navegation')
    config.set_session_factory(navegation_session_factory)

    config.scan()

    return config.make_wsgi_app()
