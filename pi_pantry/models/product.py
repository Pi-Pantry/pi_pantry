from sqlalchemy import (
    Column,
    Integer,
    String,
)

from .meta import Base


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    upc = Column(String, nullable=False, unique=True)
    name = Column(String)
    brand = Column(String)
    size = Column(String)
    category = Column(String)
    description = Column(String)
