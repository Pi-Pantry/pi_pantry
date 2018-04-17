from .meta import Base
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Table,
    Boolean
)

association_table = Table(
    'association', Base.metadata,
    Column('account_id', Integer, ForeignKey('account.id')),
    Column('product_id', Integer, ForeignKey('product.id')),
    Column('quantity', Integer),
    Column('shopping_list', Boolean, default=False),
)
