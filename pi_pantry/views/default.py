from semantics3 import Products
from pyramid.view import view_config
from pyramid.security import NO_PERMISSION_REQUIRED

<<<<<<< HEAD
=======

sem3 = Products(
    api_key="SEM3D15F366CA4EE3092E9295299DBDD45C3",
    api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
)

>>>>>>> 46bd9a372bc33c40e42871f43e56c5e34cd985ef

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
