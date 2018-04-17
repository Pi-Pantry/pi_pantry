from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    Text,
    DateTime,
    Float,
    ForeignKey,
)

from .meta import Base


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    upc = Column(String, nullable=False, unique=True)
    size = Column(String)
    name = Column(String)
    brand = Column(String)
    price = Column(Float)
