# from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.reponse import Response
from sqlalchemy.exc import DBAPIError
from ..models import Product, Account
from pyramid.view import view_config
from . import DB_ERR_MSG
from default import sem3


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
