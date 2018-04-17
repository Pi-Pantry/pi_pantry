from sqlalchemy.exc import DBAPIError
from pyramid.response import Response
from pyramid.view import view_config
from .default import sem3
from semantics3.error import Semantics3Error
# import requests


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
    renderer='../templates/manage_item.jinja2')
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
        if upc_data is None:
            try:
                sem3.products_field("upc", upc)
                query_data = sem3.get_products()
                product = parse_upc_data(query_data)
                instance = Product(**product)
            except (KeyError, IndexError, Semantics3Error):
                return {'err': '[ ! ]  INVALID UPC INPUT'}
            try:
                request.dbsession.add(instance)
            except DBAPIError:
                return Response(DB_ERR_MSG, content_type='text/plain', status=500)
        return {'product': upc_data}

    if request.method == 'POST':
        pass


DB_ERR_MSG = 'Custom Error Message Here.'
