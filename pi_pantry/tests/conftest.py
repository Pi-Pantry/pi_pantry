from pyramid.httpexceptions import HTTPNotFound
from ..views import pantry_view
from pyramid import testing
import pytest


@pytest.fixture
def dummy_request():
    return testing.DummyRequest(method="POST", status_code=200)
