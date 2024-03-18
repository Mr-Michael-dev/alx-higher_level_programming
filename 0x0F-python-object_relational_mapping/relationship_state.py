#!/usr/bin/python3

"""
This module contains the class definition of a State and
an instance Base = declarative_base() of SQLAlchemy
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City

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
    cities = relationship("City", back_populates="state")

    def __str__(self):
        return "{}: {}".format(self.id, self.name)
