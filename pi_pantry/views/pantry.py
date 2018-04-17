from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPBadRequest
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import Account, Product
from ..sample_data import MOCK_DATA
from .default import sem3
from . import DB_ERR_MSG
import requests


# @view_config(
#     route_name='pantry',
#     renderer='../templates/pantry.jinja2',
#     request_method='GET')
# def pantry_view(request):

#     try:
#         query = request.dbsession.query(Account)
#         instance = query.filter(Account.username == request.authenticated_userid).first()

#     except DBAPIError:
#         return Response(DB_ERR_MSG, content_type='text/plain', status=500)
#     if instance:
#         return {'data': instance.product_id}
#     else:
#         return HTTPNotFound()


# @view_config(
#     route_name='detail',
#     renderer='../templates/detail.jinja2',
#     request_method='GET')
# def detail_view(request):
#     """
#     Directs user to the detail template
#     """
#     try:
#         upc = request.matchdict['upc']
#     except KeyError:
#         return HTTPNotFound()

#     try:
#         query = request.dbsession(Account)
#         stock_detail = query.filter(Account.username == request.authenticated_userid).filter(
#             Product.upc == upc).one_or_none()
#     except DBAPIError:
#         return Response(DB_ERR_MSG, content_type='text/plain', status=500)

#     if stock_detail is None:
#         raise HTTPNotFound()


@view_config(
    route_name='product_detail',
    renderer='../templates/product_detail.jinja2',
    request_method='GET')
def portfolio_view(request):
    """
    Directs user to their portfolio template
    """
    return {'data': MOCK_DATA}


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
            def get_upc():
                upc = input('SCAN BARCODE: ')
                print('SUCCESSFULLY SCANNED', upc)
                return upc

            sem3.products_field("upc", get_upc())
            query_data = sem3.get_products()

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

            print(parse_upc_data(query_data))

        return {'product': upc_data}

    if request.method == 'POST':
        
        try:
            upc = request.POST['upc']
        except KeyError:
            raise HTTPBadRequest()

        query = request.dbsession.query(Account)
        user = query.filter(Account.username == request.authenticated_userid).first()

        try:
            query = request.dbsession.query(Product)
            item = query.filter(Product.upc == upc).one_or_none()
        except DBAPIError:
            return Response(DB_ERR_MSG, content_type='text/plain', status=500)

        if item is None:
            response = requests.get(API_URL + '/stock/{}/company'.format(symbol))
            product = response.json()

            instance = Product(**upc_data)
            instance.account_id.append(user)

            try:
                request.dbsession.add(instance)
            except DBAPIError:
                return Response(DB_ERR_MSG, content_type='text/plain', status=500)

        else:
            item.account_id.append(user)

