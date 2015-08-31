from pyramid.session import SignedCookieSessionFactory
from pyramid.renderers import JSONP
from pyramid.config import Configurator
from pyramid.settings import aslist, asbool

from access import controller
from thrift_clients import clients

from access.views_website import cache_region as views_website_cache_region
from access.controller import cache_region as controller_cache_region

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_renderer('jsonp', JSONP(param_name='callback', indent=4))

    hosts = aslist(settings['elasticsearch'])

    def add_index(request):
        return controller.stats(hosts=hosts, sniff_on_start=True, 
            sniff_on_connection_fail=True)

    def add_articlemeta(request):
        return controller.articlemeta(settings['articlemeta'])

    config.include('pyramid_mako')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index_web', '/')
    config.add_route('accesses_web', '/w/accesses')
    config.add_route('production_web', '/w/production')
    config.add_route('index_api', '/api')
    config.add_route('stats', '/api/v1/stats')
    config.add_route('document', '/api/v1/document')
    config.add_request_method(add_index, 'index', reify=True)
    config.add_request_method(add_articlemeta, 'articlemeta', reify=True)

    ## Cache Settings Config
    if 'memcached_host' in settings:
        cache_config = {}
        cache_config['expiration_time'] = int(settings.get('memcached_expiration_time', 3600))
        cache_config['arguments'] = {'url': settings['memcached_host'], 'binary': True}
        views_website_cache_region.configure('dogpile.cache.pylibmc', **cache_config)
        controller_cache_region.configure('dogpile.cache.pylibmc', **cache_config)
    else:
        views_website_cache_region.configure('dogpile.cache.null')
        controller_cache_reagion.configure('dogpile.cache.null')

    ## Session config
    navegation_session_factory = SignedCookieSessionFactory('sses_navegation')
    config.set_session_factory(navegation_session_factory)

    config.scan()

    return config.make_wsgi_app()
