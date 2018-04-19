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