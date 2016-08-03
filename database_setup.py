from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    name = Column(String(60))
    sir_name = Column(String(60))
    id = Column(Integer, primary_key=True)
    gender = Column(String(15))
    borth_date = Column(String)
    country = Column(String(30))
    city = Column(String(60))  # city/town name
    user_name = Column(String(60))
    password = Column(String(60))
