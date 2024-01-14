#!/usr/bin/python3
"""
This module represents a base class.
The goal is to manage id
"""


class Base:
    """
    Base class for other classes.

    Attributes:
        private class attribute: __nb_objects

    Methods:
        Instantiation method
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes instances with an id

        Arg:
            id: id of the new instance
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
