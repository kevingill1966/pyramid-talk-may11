"""
    Configuring a Route lookup (URLDispatch)

    Ref: http://docs.pylonsproject.org/projects/pyramid/1.0/narr/urldispatch.html

    This code registers this URL:

        http://localhost:8080/tut/x/y/hello

"""

from paste.httpserver import serve
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response("""Hello world from %s (%s)!<br>
        request.matchdict = %s""" % (__file__, __package__, request.matchdict))

if __name__ == '__main__':
    config = Configurator()
    config.add_route('myroute', '/tut/{one}/{two}/hello', view=hello_world)
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')

