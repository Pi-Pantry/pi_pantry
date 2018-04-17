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


# @view_config(
#     route_name='detail',
#     renderer='../templates/detail.jinja2',
#     request_method='GET')
# def detail_view(request):
#     """
#     Directs user to the detail template
#     """
#     upc = request.matchdict['upc']

#     for data in MOCK_DATA:
#         if data['upc'] == upc:
#             return {'data': data}
#     return {}
