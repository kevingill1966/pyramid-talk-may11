Pyramid Tutorial
================

This document is in RST. To generate html, you need to install docutils::

    $ pip install docutils
    $ rst2html.py tutorial.rst > tutorial.html

Create a directory in which to work.

http://docs.pylonsproject.org/projects/pyramid/1.0/narr/install.html#installing-pyramid-on-a-unix-system
::

    $ virtualenv --no-site-packages tutorial
    New python executable in tutorial/bin/python2.6
    Also creating executable in tutorial/bin/python
    Installing setuptools............done.
    $ cd tutorial
    $ . ./bin/activate
    $ pip install pyramid

Checkout the repository from git::

    $ git clone git@github.com:kevingill1966/pyramid-talk-may11.git pyramid-talk-may11.git

Quick Start (001_quickstart.py)
-------------------------------

This demonstrates:

    - Creating a view using a function (like Django) - default view
    - How to run an absolutely minimal server. (Micro framework approach)
    - Verify your installation

Simply run this code and all the single file code using the python
interpreter from your virtualenv::

    $ python 001_quickstart.py

This code registers one functions (view) on this URL:

    - http://localhost:8080/

::

    from paste.httpserver import serve
    from pyramid.config import Configurator
    from pyramid.response import Response

    def hello_world(request):
        return Response('Hello world!')

    if __name__ == '__main__':
        config = Configurator()
        config.add_view(hello_world)
        app = config.make_wsgi_app()
        serve(app, host='0.0.0.0')


Scan Source for Configuration (002_scan.py)
-------------------------------------------

This demonstrates:

    - Configuring views in code and scanning to get them
    - Introduces Traversal

This code registers one functions (view) on this URL:

    - http://localhost:8080/

::

    from paste.httpserver import serve
    from pyramid.config import Configurator
    from pyramid.response import Response
    from pyramid.view import view_config

    @view_config()
    def hello_world(request):
        return Response('Hello world!')

    if __name__ == '__main__':
        config = Configurator()
        config.scan()
        app = config.make_wsgi_app()
        serve(app, host='0.0.0.0')

Scan Source for configuration (003_urls2views.py)
-------------------------------------------------

This demonstrates:
    
    - naming a couple of views. 

This code registers two functions on three URLS:

    - http://localhost:8080/
    - http://localhost:8080/hello
    - http://localhost:8080/goodbye

::

    from paste.httpserver import serve
    from pyramid.config import Configurator
    from pyramid.response import Response
    from pyramid.view import view_config

    @view_config()
    @view_config(name='hello') 
    def hello_world(request):
        return Response('Hello world!')

    @view_config(name='goodbye')
    def goodbye_world(request):
        return Response('Goodbye world!')

    if __name__ == '__main__':
        config = Configurator()
        config.scan()
        app = config.make_wsgi_app()
        serve(app, host='0.0.0.0')

Routes (004_routes.py)
----------------------

Routes provide the mechanism to encode data into the URL (also called URLDispatch). Note the following environment variable is useful::

    PYRAMID_DEBUG_ROUTEMATCH=true

This demonstrates:

    - How to configure a URL with parts
    - How to see those parts in the view

This code registers one functions on this URL. x and y can be any values:

    http://localhost:8080/tut/x/y/hello

::

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


Routes plus Travesal (005_routes_plus_traversal.py)
---------------------------------------------------

This demonstrates:

    - Mixing a route match with a traversal

This code registers one functions on this URL. x and y can be any values:

    http://localhost:8080/tut/x/y/hello

::

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


Using template directly (006_template_direct.py)
------------------------------------------------

This demonstrates:

    - calling a template from code. (Chameleon)

Note: The template is prefixed by the module name. This is
required since we are not using a package. Normally it is not required.

You can reload the template without starting the server if you 
set this environment variable::

    PYRAMID_RELOAD_TEMPLATES=1

This code registers one view which renders directly using a template
on this URL:

    - http://localhost:8080/

::

    from paste.httpserver import serve
    from pyramid.config import Configurator
    from pyramid.renderers import render_to_response

    def hello_world(request):
        return render_to_response('006_template_direct:006_template_direct.pt',
                {'file': __file__, 'package': __package__}, request=request)

    if __name__ == '__main__':
        config = Configurator()
        config.add_view(hello_world)
        app = config.make_wsgi_app()
        serve(app, host='0.0.0.0')

Using template directly (007_template_direct.py)
------------------------------------------------

This demonstrates:

    - calling a template from code. (Jinja2)

You must install the pyramid_jinja2 package::

    $ pip install pyramid_jinja2

Note: The template is prefixed by the module name. This is
required since we are not using a package. Normally it is not required.

You can reload the template without starting the server if you 
set this environment variable::

    PYRAMID_RELOAD_TEMPLATES=1

This code registers one view which renders directly using a template
on this URL:

    - http://localhost:8080/

::

    from paste.httpserver import serve
    from pyramid.config import Configurator
    from pyramid.renderers import render_to_response

    def hello_world(request):
        return render_to_response('007_template_direct:007_template_direct.jinja2',
                {'file': __file__, 'package': __package__}, request=request)

    if __name__ == '__main__':
        config = Configurator()
        config.include('pyramid_jinja2')     # Configure must be include
        config.add_view(hello_world)
        app = config.make_wsgi_app()
        serve(app, host='0.0.0.0')

Using a renderer (008_rendered.py)
------------------------------------------------

This demonstrates:

    - using a renderer to render the code, rather than rendering directly.

This code provides these URLs:

    - http://localhost:8080
    - http://localhost:8080/jinja2
    - http://localhost:8080/chameleon
    - http://localhost:8080/json

::

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

Static Assets (009_assets.py)
-----------------------------

Static Assets are files, e.g. css, js, images etc.

This demonstrates:

    - Configuring a url path 'static' to serve content from file system

You can configure an environment variable to reload assets if changed::

    PYRAMID_RELOAD_ASSETS=1

This code provides these URLs:

    - http://localhost:8080
    - http://localhost:8080/static/pyramid-small.png

::

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

Using deform (020_deform.py)
----------------------------

Forms are not part of Pyramid. They are considered a 'library' issue
rather than a 'framework' issue.

The approach is to use different components for the form. I used:

    - deform - generates forms from a schema
    - colander - extract fields from the request

Advantages of this approach:

    - form templating is independent of templating system, i.e. inserts form intto jinja2, chameleon or mako
    - request parsing is more reusable

::

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

Using Projects
--------------

This demonstrates:

    - How to create a 'standard' project

Documentation is at:

    http://docs.pylonsproject.org/projects/pyramid/1.0/narr/project.html

Normally, Pyramid is used to create Projects. The projects boilerplate is generated using paste. List templates using the following command::

    $ paster create --list-templates
    Available templates:
    basic_package:           A basic setuptools-enabled package
    paste_deploy:            A web application deployed through paste.deploy
    pyramid_alchemy:         pyramid SQLAlchemy project using traversal
    pyramid_jinja2_starter:  pyramid jinja2 starter project
    pyramid_routesalchemy:   pyramid SQLAlchemy project using url dispatch (no traversal)
    pyramid_starter:         pyramid starter project
    pyramid_zodb:            pyramid ZODB starter project

Note: pyramid_jinja2_starter is only available after installing pyramid_jinja2.

Create a jinja2 project::

    $ paster create -t pyramid_jinja2_starter proj_010_jinja_project
    Selected and implied templates:
      pyramid-jinja2#pyramid_jinja2_starter  pyramid jinja2 starter project

    Variables:
      egg:      proj_010_jinja_project
      package:  proj_010_jinja_project
      project:  proj_010_jinja_project
    Creating template pyramid_jinja2_starter
    ...

See what has been created::

        proj_010_jinja_project/:
        |-- CHANGES.txt
        |-- development.ini 
        |-- production.ini 
        |-- proj_010_jinja_project:
        |   |-- __init__.py 
        |   |-- models.py 
        |   |-- tests.py 
        |   |-- static:
        |   |   |-- favicon.ico 
        |   |   |-- logo.png 
        |   |   |-- pylons.css
        |   |-- templates:
        |   |   |-- mytemplate.jinja2
        |   |-- views.py
        |-- README.txt 
        |-- setup.cfg
        |-- setup.py

Initialise the project::

    $ cd proj_010_jinja_project
    $ python setup.py develop

Run the project (--reload parameter optional - useful in development)::

    $ paster serve development.ini --reload
    Starting server in PID 485.
    serving on 0.0.0.0:6543 view at http://127.0.0.1:6543

It provides a URL at:

    - http://127.0.0.1:6543

Modify the file proj_010_jinja_project/templates/mytemplate.jinja2 and see
the changes take place.

* The error trace *

Modify the file proj_010_jinja_project/templates/mytemplate.jinja2 and see
the changes take place.

Modify the file to include the following errors.::

    {{ badvar/1 }}

The redisplay the page to navigate through the call stack.


* Testing *

Usual unit test stuff::

    python setup.py test

Using SQLAlchemy
----------------

Create a new project::

    $ paster create -t pyramid_routesalchemy  proj_011_alchemySelected and implied templates:
      pyramid#pyramid_routesalchemy  pyramid SQLAlchemy project using url dispatch (no traversal)

    ...

Build the project::

    $ cd proj_011_alchemy
    $ python setup.py develop

Connection information is in the .ini file::

    [app:proj_011_alchemy]
    use = egg:proj_011_alchemy
    ...
    sqlalchemy.url = sqlite:///%(here)s/proj_011_alchemy.db

The database is initialised in *proj_011_alchemy/models.py:initialize_sql* .

If you load the root URL, the view */proj_011_alchemy/views.py:my_view* .

You can include these values into the template 
*/proj_011_alchemy/templates/mytemplate.pt* 
and see values from the database::

          ${root.name}
          ${root.id}
          ${root.value}
          ${root}

*Using Alchemy Forms*


