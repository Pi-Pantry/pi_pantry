import os
import pytest
from pyramid import testing
from ..models.meta import Base
from ..models import Product, Account, Assoc


@pytest.fixture
def test_upc():
    return upc(
        '0abc0971236'
    )


# @pytest.fixture
# def configuration(request):
#     """Setup a database for testing purposes."""
#     config = testing.setUp(settings={
#         'sqlalchemy.url': os.environ['TEST_DATABASE_URL']
#     })
#     config.include('pi_pantry.models')
#     config.include('pi_pantry.routes')

#     def teardown():
#         testing.tearDown()

#     request.addfinalizer(teardown)
#     return config


@pytest.fixture
def db_session(configuration, request):
    """Create a database session for interacting with the test database."""
    SessionFactory = configuration.registry['dbsession_factory']
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture
def dummy_request(db_session):
    """Create a dummy GET request with a dbsession."""
    return testing.DummyRequest(dbsession=db_session)


@pytest.fixture
def dummy_request_bad(db_session):
    """Create a dummy GET request with a bad dbsession."""
    return data.DummyRequest(dbsession=db_session)



@pytest.fixture
def test_account():
    return Account(username='user', email='user@user.com', password='password')