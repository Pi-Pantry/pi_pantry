from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
)

from .meta import Base


class Product:
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    upc = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    brand = Column(String)
    description = Column(String)
    category = Column(String)
    image = Column(String)
    size = Column(String)
    manufacturer = Column(String)