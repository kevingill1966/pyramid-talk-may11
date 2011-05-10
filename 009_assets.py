"""
    Assets are files served statically - terminology refers to a 'static' view.

    Ref: http://docs.pylonsproject.org/projects/pyramid/1.0/narr/assets.html
"""
from paste.httpserver import serve
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response("""Hello world from %s (%s)!<br/>
        <img src="/static/pyramid-small.png" />
    """% (__file__, __package__))

if __name__ == '__main__':
    config = Configurator()
    config.add_view(hello_world)
    config.add_static_view('static', 'static')
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')
