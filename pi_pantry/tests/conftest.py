<<<<<<< HEAD
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
=======
# import os
import pytest
import unittest
from pyramid import testing
from ..models.meta import Base
from ..models import Product
from ..models import Account
from ..models import Assoc


@pytest.fixture
def test_entry():
    """
    Test stock entry
    """
    return Product(
        upc='011345876435',
        name='Huge Chocolate Bar',
        brand='HUGE',
        description='Giant chocolate bar with chocolate',
        category='candy',
        image='https://www.hugecandy.com',
        size='10 lbs',
        manufacturer='Huge candy co.',
    )


def test_account():
    """
    Test account entry
    """
    return Account(
        username='brandon',
        password='1234',
        email='brandon@brandon.brandon'
    )


@pytest.fixture
def configuration(request):
    """
    Setup a database for testing purposes
    """
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres://localhost:5432/pantry_test'
        # 'sqlalchemy.url': os.environ['TEST_DATABASE_URL']
    })
    config.include('pi_pantry.models')
    config.include('pi_pantry.routes')

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config
>>>>>>> d5adbac3606f0816e91e163bdae2d93d445eb58d


@pytest.fixture
def db_session(configuration, request):
<<<<<<< HEAD
    """Create a database session for interacting with the test database."""
=======
    """
    Create a database session for interacting with the test database
    """
>>>>>>> d5adbac3606f0816e91e163bdae2d93d445eb58d
    SessionFactory = configuration.registry['dbsession_factory']
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session
<<<<<<< HEAD


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
=======


@pytest.fixture
def dummy_request(db_session):
    """
    Create a dummy GET request with a dbsession
    """
    return testing.DummyRequest(dbsession=db_session)
>>>>>>> d5adbac3606f0816e91e163bdae2d93d445eb58d
