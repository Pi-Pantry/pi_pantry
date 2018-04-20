import os
import pytest
import unittest
from pyramid import testing
from ..models.meta import Base
from ..models import Account
from ..models import Product
from ..models import Assoc


@pytest.fixture
def new_entry():
    """
    Test product entry
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


@pytest.fixture
def account_entry():
    """
    Test account entry
    """
    return Account(
        username='brandon',
        password='1234',
        email='brandon@brandon.brandon'
    )


@pytest.fixture
def assoc_entry():
    """
    Test association
    """
    return Assoc(
        account_id='1',
        product_id='1',
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

    config.testing_securitypolicy(
        userid="brandon",
        permissive=True,
    )

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture
def db_session(configuration, request):
    """
    Create a database session for interacting with the test database
    """
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
    """
    Create a dummy GET request with a dbsession
    """
    return testing.DummyRequest(dbsession=db_session)


@pytest.fixture
def add_items(dummy_request, test_entries):
    """
    Create a new Entry and add to database
    """
    dummy_request.dbsession.add_all(test_entries)
    return test_entries


@pytest.fixture(scope='session')
def test_entries():
    """
    Create a list of Entry objects to be added to the database
    """
    return [
        Product(
            upc='011345876435',
            name='Huge Chocolate Bar',
            brand='HUGE',
            description='Giant chocolate bar with chocolate',
            category='candy',
            image='https://www.hugecandy.com',
            size='10 lbs',
            manufacturer='Huge candy co.',
        ) for i in range(20)
    ]
