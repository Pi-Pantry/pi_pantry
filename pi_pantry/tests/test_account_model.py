
def test_constructed_account_correct_username(db_session):
    from ..models import Account

    assert len(db_session.query(Account).all()) == 0
    account = Account(username='brandon', email='brandon@brandon.brandon', password='1234')
    db_session.add(account)
    assert len(db_session.query(Account).all()) == 1


def test_create_account_without_username(db_session):
    from ..models import Account
    import pytest

    with pytest.raises(Exception):
        return Account(email='brandon@brandon.brandon', password='1234')


def test_duplicate(db_session):
    from sqlalchemy.exc import IntegrityError
    import pytest
    from ..models import Account
    account = Account(username='brandon', email='brandon@brandon.brandon', password='1234')
    account_two = Account(username='brandon', email='brandon@brandon.brandon', password='1234')
    db_session.add(account)
    db_session.commit()
    with pytest.raises(IntegrityError):
        db_session.add(account_two)
        db_session.flush()
