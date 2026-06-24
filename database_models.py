from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, Float

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    