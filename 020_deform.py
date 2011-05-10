"""
    Simple form using deform + collander
    
    Ref: http://docs.pylonsproject.org/projects/deform/dev/
    Ref: http://docs.pylonsproject.org/projects/colander/dev/
"""
from paste.httpserver import serve
from pyramid.config import Configurator
from pyramid.response import Response

import deform
import colander

class Schema(colander.MappingSchema):
    firstname = colander.SchemaNode(colander.String(), title=u'First Name')
    lastname = colander.SchemaNode(colander.String(), title=u'Last Name')


def hello_world(request):
    form = deform.Form(Schema(), buttons=(
        deform.Button('submit', 'Say Hello'),))

    if 'submit' in request.POST:
        try:
            appstruct = form.validate(request.params.items())
            return Response('Hello <b>%s %s</b> from %s (%s)!' % (
                request.params['firstname'], request.params['lastname'], __file__, __package__))
        except deform.ValidationFailure, e:
            return Response(e.render())
    else:
        return Response(form.render())

if __name__ == '__main__':
    config = Configurator()
    config.add_view(hello_world)
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')
