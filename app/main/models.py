from sqlalchemy import Column, Integer
from db_create import Base

class Click(Base):
    """"""
    __tablename__ = "albums"

    id = Column(Integer, primary_key = True)
    count = Column('count', Integer)

    def __repr__(self):
        return '<Click %r>' % (self.count)