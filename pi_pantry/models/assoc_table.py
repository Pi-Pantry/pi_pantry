from .meta import Base
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Table,
)

association_table = Table('association', Base.metadata,
                          Column('account_id', Integer, ForeignKey('account.id')),
                          Column('product_id', Integer, ForeignKey('product.id'))
                          )
