from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPBadRequest
from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import Account, Product
from ..models.association import association_table
from . import DB_ERR_MSG
import requests


API_URL = ''


@view_config(route_name='pantry', renderer='../templates/pantry.jinja2', request_method='GET')
def entries_view(request):

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
        upc = request.matchdict['upc']
    except KeyError:
        return HTTPNotFound()

    try:
        query = request.dbsession.query(Product)
        stock_detail = query.filter(Stock.account_id == request.authenticated_userid).filter(Stock.symbol == stock_symbol).one_or_none()

    except DBAPIError:
        return Response(DB_ERR_MSG, content_type='text/plain', status=500)

    for each in stock_detail:
       if each.username == request.authenticated_userid:
           return {'stock': stock_detail}
