from pyramid.view import notfound_view_config


@notfound_view_config(
    renderer='../templates/404.jinja2'
)
def notfound_view(request):
    """Returns 404 status if an endpoint was not found in routes"""
    request.response.status = 404
    return {}
