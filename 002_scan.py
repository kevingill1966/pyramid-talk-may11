"""
    Demonstrates scanning for declarations

    Ref: http://docs.pylonsproject.org/projects/pyramid/1.0/narr/configuration.html#configuration-decorations-and-code-scanning

    This code registers one functions on the default URLt

        http://localhost:8080/
"""

from paste.httpserver import serve
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config                # NEW

@view_config()                                      # NEW
def hello_world(request):
    return Response('Hello world from %s (%s)!' % (__file__, __package__))

if __name__ == '__main__':
    config = Configurator()
    #config.add_view(hello_world)                   # REMOVED
    config.scan()
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')
