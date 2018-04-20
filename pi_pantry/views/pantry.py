from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPClientError
from semantics3.error import Semantics3Error
from sqlalchemy.exc import DBAPIError
from pyramid.response import Response
from pyramid.view import view_config
from ..models import Account
from ..models import Product
from ..models import Assoc
from .default import sem3
from . import DB_ERR_MSG


@view_config(
    route_name='pantry',
    renderer='../templates/pantry.jinja2',
    request_method='GET',
    )
def pantry_view(request):
    """
    Pantry View displays the current user's data. Users here can manage their
    pantry items from their cart to pantry or vice versa. On addition users can
    remove products.
    """
    try:
        query = request.dbsession.query(Account)
        current_account = query.filter(
            Account.username == request.authenticated_userid).first()
    except DBAPIError:
        return DBAPIError(DB_ERR_MSG, content_type='text/plain', status=500)

    pantry, cart = [], []
    for assoc in current_account.pantry_items:
        if assoc.in_pantry:
            pantry.append(assoc.item)
        if assoc.in_cart:
            cart.append(assoc.item)

    return {'pantry': pantry, 'cart': cart}


@view_config(
    route_name='detail',
    renderer='../templates/detail.jinja2',
    request_method='GET',
)
def detail_view(request):
    """
    Fetches current users data from junction table and displays product
    specific details.
    """

    if 'upc' not in request.matchdict:
        return HTTPClientError()
    upc = request.matchdict['upc']
    user = request.dbsession.query(Account).filter(
        Account.username == request.authenticated_userid).first()
    item = filter(lambda n: n.item.upc == upc, user.pantry_items)
    try:
        product = next(item)
    except StopIteration:
        raise HTTPNotFound

    return {'item': product.item}


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
    request_method=('GET', 'POST'))
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
        acc_query = request.dbsession.query(Account)
        current_acc = acc_query.filter(
            Account.username == request.authenticated_userid).first()

        if upc_data is None:
            try:
                sem3.products_field("upc", upc)
                query_data = sem3.get_products()
                product = parse_upc_data(query_data)
                upc_data = Product(**product)
            except (KeyError, IndexError, Semantics3Error):
                return {'err': '[ ! ]  INVALID UPC INPUT'}
            try:
                request.dbsession.add(upc_data)
            except DBAPIError:
                return Response(DB_ERR_MSG,
                                content_type='text/plain', status=500)

        location = request.GET.getall('location')
        in_pantry = in_cart = False
        if 'both' in location:
            in_pantry = True
            in_cart = True

        if 'pantry' in location:
            in_pantry = True

        if 'cart' in location:
            in_cart = True

        for assoc in current_acc.pantry_items:
            if upc == assoc.item.upc:
                break
        else:
            assoc = Assoc()
            assoc.item = upc_data
            current_acc.pantry_items.append(assoc)

        assoc.in_cart = in_cart
        assoc.in_pantry = in_pantry
        request.dbsession.flush()
        return HTTPFound(location=request.route_url('pantry'))

    if request.method == 'POST':
        try:
            upc = request.POST['upc']
        except KeyError:
            print('KeyError')
            return {}
        acc_query = request.dbsession.query(Account)
        current_acc = acc_query.filter(
            Account.username == request.authenticated_userid).first()
        for assoc in current_acc.pantry_items:
            if upc == assoc.item.upc:
                break
        if 'cart' in request.POST:
            assoc.in_cart = False
        if 'pantry' in request.POST:
            assoc.in_pantry = False
        request.dbsession.flush()
        return HTTPFound(location=request.route_url('pantry'))
