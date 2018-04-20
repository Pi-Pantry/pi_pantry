import pytest


def test_default_behavior_of_base_view(dummy_request):
    """
    test base view status and type
    """
    from ..views.default import index_view
    response = index_view(dummy_request)
    assert type(response) == dict


def test_default_response_index_view(dummy_request):
    """
    test home view
    """
    from ..views.default import index_view
    response = index_view(dummy_request)
    assert len(response) == 0
    assert type(response) == dict


def test_default_response_pantry_view_bad_db(dummy_request):
    """
    test manage_items_view
    """
    from ..views.pantry import manage_items_view
    dummy_request.GET = {'key': 'value'}
    response = manage_items_view(dummy_request)
    assert response == {}


def test_default_notfound__(dummy_request):
    """
    test 404_view
    """
    from ..views.notfound import notfound_view
    response = notfound_view(dummy_request)
    assert response == {}


def test_semple_data_():
    """
    test data
    """
    from ..sample_data.__init__ import MOCK_DATA
    assert type(MOCK_DATA) == list


def test_detail_retrieval(dummy_request, db_session, new_entry, account_entry):
    from ..views.pantry import detail_view

    new_entry.account_id.append(account_entry)
    db_session.add(new_entry)
    db_session.add(account_entry)

    # db_session.flush()

    dummy_request.matchdict = {'name': 'fake'}
    response = detail_view(dummy_request)
    assert type(response) == dict
    assert response['data'].upc == 'fake'


def test_item_adds_to_database(dummy_request, db_session):
    """
    test add item to pantry adds to database
    """
    from ..views.pantry import manage_items_view
    from ..models import Product

    dummy_request.method = 'POST'
    dummy_request.POST['upc'] = '123456789098'
    manage_items_view(dummy_request)
    query = db_session.query(Product)
    first = query.filter(Product.upc == '123456789098').first()
    assert first.upc == '123456789098'
    assert first.name == 'Test'
