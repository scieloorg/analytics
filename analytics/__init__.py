from pyramid.session import SignedCookieSessionFactory
from pyramid.renderers import JSONP
from pyramid.config import Configurator
from pyramid.settings import aslist, asbool

from analytics import controller
from thrift_clients import clients

from analytics.views_website import cache_region as views_website_cache_region
from analytics.controller import cache_region as controller_cache_region

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_renderer('jsonp', JSONP(param_name='callback', indent=4))

    def add_accessstats(request):
        return controller.accessstats(settings['accessstats'])

    def add_publicationstats(request):
        return controller.publicationstats(settings['publicationstats'])

    def add_articlemeta(request):
        return controller.articlemeta(settings['articlemeta'])

    config.include('pyramid_mako')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index_web', '/')
    config.add_route('accesses_web', '/w/accesses')
    config.add_route('accesses_bydocumenttype', '/ajx/accesses/bydocumenttype')
    config.add_route('accesses_bymonthandyear', '/ajx/accesses/bymonthandyear')
    config.add_route('accesses_lifetime', '/ajx/accesses/lifetime')
    config.add_route('publication_web', '/w/publication')
    config.add_route('publication_article_licenses', '/ajx/publication/article_licenses')
    config.add_route('publication_article_references', '/ajx/publication/article_references')
    config.add_route('publication_article_languages', '/ajx/publication/article_languages')
    config.add_route('publication_article_authors', '/ajx/publication/article_authors')
    config.add_route('publication_article_affiliations', '/ajx/publication/article_affiliations')
    config.add_route('publication_article_year', '/ajx/publication/article_year')
    config.add_route('publication_article_subject_areas', '/ajx/publication/article_subject_areas')
    config.add_request_method(add_accessstats, 'accessstats', reify=True)
    config.add_request_method(add_articlemeta, 'articlemeta', reify=True)
    config.add_request_method(add_publicationstats, 'publicationstats', reify=True)

    ## Cache Settings Config
    if 'memcached_host' in settings:
        cache_config = {}
        cache_config['expiration_time'] = int(settings.get('memcached_expiration_time', 3600))
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
