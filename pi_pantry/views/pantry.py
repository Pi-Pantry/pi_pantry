<<<<<<< HEAD
from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPBadRequest
from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import Account, Product
from ..models.association import association_table
from . import DB_ERR_MSG
import requests


@view_config(route_name='pantry', renderer='../templates/pantry.jinja2', request_method='GET')
def pantry_view(request):

    try:
        query = request.dbsession.query(Account)
        instance = query.filter(Account.username == request.authenticated_userid).first()

    except DBAPIError:
        return Response(DB_ERR_MSG, content_type='text/plain', status=500)
    if instance:
        return {'data': instance.product_id}
    else:
        return HTTPNotFound()


@view_config(route_name='detail', renderer='../templates/product-detail.jinja2', request_method='GET')
def detail_view(request):
    try:
        product_id = request.matchdict['id']
    except KeyError:
        return HTTPNotFound()

    try:
        query = request.dbsession.query(Product)
        product_detail = query.filter(Product.account_id == request.authenticated_userid).filter(Product.id == product_id).one_or_none()

    except DBAPIError:
        return Response(DB_ERR_MSG, content_type='text/plain', status=500)

    for each in product_detail:
        if each.username == request.authenticated_userid:
            return {'product': product_detail}


@view_config(route_name='pantry', renderer='../templates/shopping_list.jinja2', request_method='GET')
def shopping_view(request):

    try:
        query = request.dbsession.query(Account)
        instance = query.filter(Account.username == request.authenticated_userid).first() and Account.shopping_list is True

    except DBAPIError:
        return Response(DB_ERR_MSG, content_type='text/plain', status=500)
    if instance:
        return {'product': instance.product_id}
    else:
        return HTTPNotFound()
=======
from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.view import view_config
from default import sem3


@view_config(
    route_name='manage_item',
    renderer='../templates/manage_item.jinja2',
    request_method=('POST', 'DELETE'),
    permission=NO_PERMISSION_REQUIRED,)
def add_item(request):
    # UPLOAD ITEM TO USERS ACCOUNT
    if request.method == 'POST':
        try:
            item_upc = request.GET['upc']
        except KeyError:
            return {}
    # Delete item from users pantry
    if request.method == 'DELETE':
        pass
>>>>>>> 46bd9a372bc33c40e42871f43e56c5e34cd985ef
