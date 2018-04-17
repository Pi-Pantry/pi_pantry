from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from .assoc_table import association_table
from .meta import Base


class Product:
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    account = relationship('Account', secondary=association_table)
    upc = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    brand = Column(String)
    description = Column(String)
    category = Column(String)
    image = Column(String)
    size = Column(String)
    manufacturer = Column(String)