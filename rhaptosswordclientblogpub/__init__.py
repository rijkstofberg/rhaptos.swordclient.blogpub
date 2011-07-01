import logging
from pyramid.config import Configurator


logging.basicConfig()
log = logging.getLogger('rhaptos.swordclient.blogpub')

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # configuration setup
    config = Configurator(settings=settings)
    
    # routes setup
    config.add_route('publish_blog', '/')
    config.add_route('results', '/results')

    # static view setup
    config.add_static_view('static', 'rhaptosswordclientblogpub:static')

    # scan for @view_config and @subscriber decorators
    config.scan()
    return config.make_wsgi_app()
