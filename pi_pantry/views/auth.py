from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPBadRequest, HTTPUnauthorized, HTTPConflict
from pyramid.security import NO_PERMISSION_REQUIRED, remember, forget
from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import DBAPIError, IntegrityError
from ..models import Stock
from ..models import Account
from . import DB_ERROR_MSG
import requests

API_URL = ''


@view_config(
    route_name='auth',
    renderer='../templates/auth.jinja2',
    permission=NO_PERMISSION_REQUIRED)
def auth_view(request):
    """
    Directs user to authorization template and redirects to portfolio page on success
    """
    if request.method == 'POST':
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
        except KeyError:
            return HTTPBadRequest()

        try:
            instance = Account(
                username=username,
                email=email,
                password=password,
            )

            headers = remember(request, userid=instance.username)
            try:
                request.dbsession.add(instance)
                request.dbsession.flush()
            except IntegrityError:
                return HTTPConflict

            return HTTPFound(location=request.route_url('portfolio'), headers=headers)
        except DBAPIError:
            return Response(DB_ERROR_MSG, content_type='text/plain', status=500)

    if request.method == 'GET':
        try:
            username = request.GET['username']
            password = request.GET['password']
        except KeyError:
            return {}

        is_authenticated = Account.check_credentials(
            request, username, password)
        if is_authenticated[0]:
            headers = remember(request, userid=username)
            return HTTPFound(location=request.route_url('pantry'), headers=headers)
        else:
            return HTTPUnauthorized
    return HTTPFound(location=request.route_url('home'))


@view_config(route_name='logout', permission=NO_PERMISSION_REQUIRED)
def logout(request):
    """
    Logs user out and returns to home view
    """
    headers = forget(request)
    return HTTPFound(location=request.route_url('home'), headers=headers)
