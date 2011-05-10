"""
    Imperative configuration

    Ref: http://docs.pylonsproject.org/projects/pyramid/1.0/narr/configuration.html
"""
from paste.httpserver import serve
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('Hello world from %s (%s)!' % (__file__, __package__))

if __name__ == '__main__':
    config = Configurator()
    config.add_view(hello_world)
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')
