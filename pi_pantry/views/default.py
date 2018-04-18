from semantics3 import Products
# from pyramid.view import view_config
# from pyramid.security import NO_PERMISSION_REQUIRED

from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPBadRequest
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import Account, Product
from ..sample_data import MOCK_DATA
from . import DB_ERR_MSG
import requests


sem3 = Products(
    api_key="SEM3D15F366CA4EE3092E9295299DBDD45C3",
    api_secret="NGYzMjliNzlmZTRiODQ5YWE1NzI4MzdiNjMyZDNkNDE"
)


@view_config(
    route_name='home',
    renderer='../templates/base.jinja2',
    request_method='GET',
    permission=NO_PERMISSION_REQUIRED,
)
def home_view(request):
    """
    Directs user to the home template
    """
    return {}


@view_config(
    route_name='product_detail',
    renderer='..template/product_detail.jinja2',
    request_method='GET'
)
def detail_view(request):
    return {'data': MOCK_DATA}
