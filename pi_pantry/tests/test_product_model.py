def test_constructed_stock_correct_username(db_session):
    from ..models import Product

    assert len(db_session.query(Product).all()) == 0
    product = Product(upc='123456789102', name='User')
    db_session.add(product)
    assert len(db_session.query(Product).all()) == 1


def test_duplicate(db_session):
    from sqlalchemy.exc import IntegrityError
    import pytest
    from ..models import Product
    product = Product(upc='123456789102', name='User')
    product_two = Product(upc='123456789102', name='User')
    db_session.add(product)
    db_session.commit()
    with pytest.raises(IntegrityError):
        db_session.add(product_two)
        db_session.flush()
