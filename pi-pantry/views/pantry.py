from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPBadRequest
from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import Account, Stock
from ..models.association import association_table
from . import DB_ERR_MSG
import requests


API_URL = 'https://api.iextrading.com/1.0'


@view_config(route_name='pantry', renderer='../templates/pantry.jinja2', request_method='GET')
def entries_view(request):

    try:
        query = request.dbsession.query(Account)
        instance = query.filter(Account.username == request.authenticated_userid).first()

    except DBAPIError:
        return Response(DB_ERR_MSG, content_type='text/plain', status=500)
    if instance:
        return {'data': instance.stock_id}
    else:
        return HTTPNotFound()

@view_config(route_name='detail', renderer='../templates/product-detail.jinja2', request_method='GET')
def detail_view(request):
    try:
        stock_symbol = request.matchdict['symbol']
    except KeyError:
        return HTTPNotFound()

    try:
        query = request.dbsession.query(Stock)
        stock_detail = query.filter(Stock.account_id == request.authenticated_userid).filter(Stock.symbol == stock_symbol).one_or_none()

    except DBAPIError:
        return Response(DB_ERR_MSG, content_type='text/plain', status=500)

    for each in stock_detail:
       if each.username == request.authenticated_userid:
           return {'stock': stock_detail}


@view_config(route_name='add', renderer='../templates/add-item.jinja2')
def my_add_view(request):
    """This alows the customer to query the API with the UPC and returns the product information. The customer can then add that product to their pantry and get passed to the pantry page"""

    if request.method == 'GET':
        try:
            symbol = request.GET['upc']
        except KeyError:
                return {}

        try:
            query = request.dbsession.query({Product})
            company = query.filter(upc == upc).one_or_none()
        except DBAPIError:
            return Response(DB_ERR_MSG, content_type='text/plain', status=500)

        if company is None:
            response = requests.get(API_URL + '/stock/{}/company'.format(symbol))
            company = response.json()

        return {'data': company}

    if request.method == 'POST':

        try:
            symbol = request.POST['symbol']
        except KeyError:
            raise HTTPBadRequest()

        query = request.dbsession.query(Account)
        user = query.filter(Account.username == request.authenticated_userid).first()

        try:
            query = request.dbsession.query(Stock)
            company = query.filter(Stock.symbol == symbol).one_or_none()
        except DBAPIError:
            return Response(DB_ERR_MSG, content_type='text/plain', status=500)

        if company is None:
            response = requests.get(API_URL + '/stock/{}/company'.format(symbol))
            company = response.json()

            instance = Stock(**company)
            instance.account_id.append(user)

            try:
                request.dbsession.add(instance)
            except DBAPIError:
                return Response(DB_ERR_MSG, content_type='text/plain', status=500)

        else:
            company.account_id.append(user)
