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


@view_config(
    route_name='add',
    renderer='../templates/manage_items.jinja2')
def manage_items_view(request):
    if request.method == 'GET':
        try:
            upc = request.GET['upc']
        except KeyError:
            return {}
        try:
            query = request.dbsession.query(Product)
            upc_data = query.filter(Product.upc == upc).one_or_none()
        except DBAPIError:
            return Response(DB_ERR_MSG, content_type='text/plain', status=500)

        if upc_data is None:
            pass

        return {'product': upc_data}
