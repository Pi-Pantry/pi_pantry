from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.view import view_config


@view_config(
    route_name='manage_items',
    renderer='../templates/manage_items.jinja2',
    request_method=('GET', 'POST'),
    permission=NO_PERMISSION_REQUIRED,)
def index_view(request):

    return {}
