from .meta import Base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Table,
    Boolean,
)


class Assoc(Base):
    __tablename__ = 'assoc'
    account_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    in_cart = Column(Boolean, nullable=False)
    in_pantry = Column(Boolean, nullable=False)
    item = relationship('Product')
