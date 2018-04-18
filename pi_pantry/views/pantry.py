from sqlalchemy.exc import DBAPIError
from pyramid.response import Response
from pyramid.view import view_config
from semantics3.error import Semantics3Error
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPBadRequest
from pyramid.security import NO_PERMISSION_REQUIRED, remember, forget
from ..sample_data import MOCK_DATA
from . import DB_ERR_MSG
import requests
import json
from ..models import Account
from ..models import Product
from .default import sem3


@view_config(
    route_name='pantry',
    renderer='../templates/pantry.jinja2',
    request_method='GET',
    permission=NO_PERMISSION_REQUIRED)
def pantry_view(request):
    """
    Directs user to their pantry
    """
    try:
        query = request.dbsession.query(Account)
        current_account = query.filter(Account.username == request.authenticated_userid).first()
    except DBAPIError:
        return DBAPIError(DB_ERR_MSG, content_type='text/plain', status=500)

    return {'data': current_account.pantry_items}


@view_config(
    route_name='detail',
    renderer='../templates/detail.jinja2',
    request_method='GET',
    permission=NO_PERMISSION_REQUIRED)
def detail_view(request):
    """
    Directs user to a detailed view of an item
    """
    try:
        upc = request.matchdict['upc']
    except KeyError:
        return HTTPNotFound()

    try:
        query = request.dbsession(Account)
        product_detail = query.filter(Account.username == request.authenticated_userid).filter(
            Product.upc == upc).one_or_none()
    except DBAPIError:
        return Response(DB_ERR_MSG, content_type='text/plain', status=500)

    if product_detail is None:
        raise HTTPNotFound()


def parse_upc_data(data):
    upc_data = {
        'upc': data['results'][0]['upc'],
        'name': data['results'][0]['name'],
        'brand': data['results'][0]['brand'],
        'description': data['results'][0]['description'],
        'category': data['results'][0]['category'],
        'image': data['results'][0]['images'],
        'size': data['results'][0]['size'],
        'manufacturer': data['results'][0]['manufacturer'],
    }
    return upc_data


@view_config(
    route_name='manage_item',
    renderer='../templates/manage_item.jinja2',
    request_method='GET')
def manage_items_view(request):
    if request.method == 'GET':
        try:
            upc = request.GET['upc']
        except KeyError:
            return {}
        # try:
        query = request.dbsession.query(Product)
        upc_data = query.filter(Product.upc == upc).one_or_none()
        # except DBAPIError:
        #     return Response(DB_ERR_MSG, content_type='text/plain', status=500)

        acc_query = request.dbsession.query(Account)
        current_acc = acc_query.filter(Account.username == request.authenticated_userid).first()

        if upc_data is None:
            try:
                sem3.products_field("upc", upc)
                query_data = sem3.get_products()
                upc_data = parse_upc_data(query_data)
                instance = Product(**upc_data)
            except (KeyError, IndexError, Semantics3Error):
                return {'err': '[ ! ]  INVALID UPC INPUT'}
            try:
                request.dbsession.add(instance)
            except DBAPIError:
                return Response(DB_ERR_MSG, content_type='text/plain', status=500)
        return {'product': upc_data}

    current_acc.pantry_items.append(upc_data)
    return HTTPFound(location=request.route_url('pantry'))


