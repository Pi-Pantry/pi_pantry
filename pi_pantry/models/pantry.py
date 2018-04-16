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


class Pantry:
    __tablename__ = 'pantry'
    id = Column(Integer, primary_key=True)
    upc = Column(String, nullable=False, unique=True)
    upc_data = Column(String)
    quantity = Column(Integer)
