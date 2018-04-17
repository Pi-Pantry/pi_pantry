from semantics3 import Products
from pyramid.view import view_config
from pyramid.security import NO_PERMISSION_REQUIRED


sem3 = Products(
    api_key="SEM3D15F366CA4EE3092E9295299DBDD45C3",
    api_secret="NGYzMjliNzlmZTRiODQ5YWE1NzI4MzdiNjMyZDNkNDE"
)


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
