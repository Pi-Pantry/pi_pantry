from pyramid.view import view_config
from pyramid.security import NO_PERMISSION_REQUIRED

API_URL = ''


@view_config(
    route_name='home',
    renderer='../templates/base.jinja2',
    request_method='GET',
    permission=NO_PERMISSION_REQUIRED,)
def index_view(request):
    """
    Directs user to the home template
    """
    return {}
