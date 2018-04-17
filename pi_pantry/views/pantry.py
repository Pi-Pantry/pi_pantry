# from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.response import Response
from sqlalchemy.exc import DBAPIError
# from ..models import Product, Account
from pyramid.view import view_config
from .default import sem3


# @view_config(
#     route_name='add',
#     renderer='../templates/manage_items.jinja2')
# def manage_items_view(request):
#     if request.method == 'GET':
#         try:
#             upc = request.GET['upc']
#         except KeyError:
#             return {}
#         try:
#             query = request.dbsession.query(Product)
#             upc_data = query.filter(Product.upc == upc).one_or_none()
#         except DBAPIError:
#             return Response(DB_ERR_MSG, content_type='text/plain', status=500)
#
#         if upc_data is None:
#             def get_upc():
#                 upc = input('SCAN BARCODE: ')
#                 print('SUCCESSFULLY SCANNED', upc)
#                 return upc
#
#             sem3.products_field("upc", get_upc())
#             query_data = sem3.get_products()
#
#             def parse_upc_data(data):
#                 upc_data = {
#                     'upc': data['results'][0]['upc'],
#                     'name': data['results'][0]['name'],
#                     'brand': data['results'][0]['brand'],
#                     'description': data['results'][0]['description'],
#                     'category': data['results'][0]['category'],
#                     'image': data['results'][0]['images'],
#                     'size': data['results'][0]['size'],
#                     'manufacturer': data['results'][0]['manufacturer'],
#                 }
#                 return upc_data
#
#             print(parse_upc_data(query_data))
#
#         return {'product': upc_data}
#
#     if request.method == 'POST':
#         pass
