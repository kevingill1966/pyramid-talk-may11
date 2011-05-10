"""
    Using a template directly - Jinja2

    Ref: http://docs.pylonsproject.org/projects/pyramid/1.0/narr/templates.html
"""

from paste.httpserver import serve
from pyramid.config import Configurator
from pyramid.renderers import render_to_response

def hello_world(request):
    return render_to_response('007_template_direct:007_template_direct.jinja2',
            {'file': __file__, 'package': __package__}, request=request)

if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_jinja2')
    config.add_view(hello_world)
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')
