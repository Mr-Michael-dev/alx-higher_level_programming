#!/usr/bin/python3

"""
This module contains the class definition of a City
Inherits from Base imported from model_state.py
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey


class City(Base):
    """City Class, inherits table metadata from Base

    Attributes:
        __tablename__: defines the table name
        id: unique id for each State instance
        name: name of the state
        state_id: foreign key to state.id
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)

    def __str__(self):
        return "{}: {}".format(self.id, self.name)
