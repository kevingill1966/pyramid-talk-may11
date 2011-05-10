"""
    Demonstrates naming a couple of views. 

    Ref: http://docs.pylonsproject.org/projects/pyramid/1.0/narr/configuration.html#configuration-decorations-and-code-scanning

    This code registers two functions on three URLS

        http://localhost:8080/
        http://localhost:8080/hello
        http://localhost:8080/goodbye
"""

from paste.httpserver import serve
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

@view_config()                                                                      # NEW
@view_config(name='hello')                                                          # NEW
def hello_world(request):
    return Response('Hello world from %s (%s)!' % (__file__, __package__))

@view_config(name='goodbye')                                                        # NEW
def goodbye_world(request):                                                         # NEW
    return Response('Goodbye  world from %s (%s)!' % (__file__, __package__))       # NEW

if __name__ == '__main__':
    config = Configurator()
    config.scan()
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')
