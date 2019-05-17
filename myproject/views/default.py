from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'myproject'}


@view_config(route_name='victor', renderer='../templates/victor.jinja2')
def victor(request):
    return {'project': 'myproject'}


@view_config(route_name='outra', renderer='../templates/outra.jinja2')
def outra(request):
    return {'project': 'myproject'}
