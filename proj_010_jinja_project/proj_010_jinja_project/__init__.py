from pyramid.config import Configurator
from pyramid_jinja2 import renderer_factory
from proj_010_jinja_project.models import get_root

def main(global_config, **settings):
    """ This function returns a WSGI application.
    
    It is usually called by the PasteDeploy framework during 
    ``paster serve``.
    """
    config = Configurator(root_factory=get_root, settings=settings)
    config.add_renderer('.jinja2', renderer_factory)
    config.add_static_view('static', 'static')
    config.add_view('proj_010_jinja_project.views.my_view',
                    context='proj_010_jinja_project.models.MyModel', 
                    renderer="mytemplate.jinja2")
    return config.make_wsgi_app()
