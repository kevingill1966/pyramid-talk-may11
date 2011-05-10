"""
    Configuring a Route and view lookup (URLDispatch / Traversal hybrid)

    Ref: http://docs.pylonsproject.org/projects/pyramid/1.0/narr/hybrid.html#hybrid-chapter

    This code registers one URL:

        http://localhost:8080/tut/x/y

"""

from paste.httpserver import serve
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

@view_config(name='hello', route_name='myroute')
def hello_world(request):
    return Response("""Hello world from %s (%s)!<br>
        request.matchdict = %s""" % (__file__, __package__, request.matchdict))

if __name__ == '__main__':
    config = Configurator()
    config.add_route('myroute', '/tut/{one}/{two}/*traverse')
    config.scan()
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')

