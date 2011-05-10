"""
    Rendering the view results using a configured renderer

    Ref: http://docs.pylonsproject.org/projects/pyramid/1.0/narr/renderers.html

    Urls:
        http://localhost:8080/
        http://localhost:8080/jinja2
        http://localhost:8080/chameleon
        http://localhost:8080/json
"""

from paste.httpserver import serve
from pyramid.config import Configurator

def hello_world(request):
    return {'file': __file__, 'package': __package__}

if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_jinja2')
    config.add_view(hello_world, renderer='007_template_direct:007_rendered.jinja2')
    config.add_view(hello_world, name="jinja2", renderer='008_rendered:007_template_direct.jinja2')
    config.add_view(hello_world, name="chameleon", renderer='008_rendered:006_template_direct.pt')
    config.add_view(hello_world, name="json", renderer='json')
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')
