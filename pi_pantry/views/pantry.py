from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.view import view_config
from default import sem3


@view_config(
    route_name='manage_item',
    renderer='../templates/manage_item.jinja2',
    request_method=('POST', 'DELETE'),
    permission=NO_PERMISSION_REQUIRED,)
def add_item(request):
    # UPLOAD ITEM TO USERS ACCOUNT
    if request.method == 'POST':
        try:
            item_upc = request.GET['upc']
        except KeyError:
            return {}
    # Delete item from users pantry
    if request.method == 'DELETE':
        pass
