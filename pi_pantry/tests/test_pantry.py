# from pyramid.httpexceptions import HTTPNotFound
# from ..views.pantry import pantry_view
# Testing cases for Pantry.py


def test_pantry_view_(dummy_request):
    from ..views.pantry import pantry_view

    response = pantry_view(dummy_request)
    
    assert pantry['size'] == '1 oz.'
    assert pantry['brand'] == 'Zone'


# def test_upc_not_found():
#     """test DBAPIError for no database"""

#     response = get_portfolio_view(dummy_request_bad)
#     assert isinstance(response, HTTPNotFound)

# def test_upc_found():
#     pass


# def test_item_added():
#     pass


# def test_item_not_found():
#     pass

