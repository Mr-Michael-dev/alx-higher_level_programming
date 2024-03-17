#!/usr/bin/python3

"""
This module contains the class definition of a State and
an instance Base = declarative_base() of SQLAlchemy
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State Class, inherits table metadata from Base

    Attributes:
        __tablename__: defines the table name
        id: unique id for each State instance
        name: name of the state
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
