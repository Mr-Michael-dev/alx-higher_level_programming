#!/usr/bin/python3
"""
This module defines a BaseGeometry class
"""


class BaseGeometry:
    """
    This class represents a BaseGeometry

    Methods:
    Area raises an exception
    """

    def area(self):
        """
        Raises an Exception with a message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates value

        Name; name of value always a string
        Value: to be validated. must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
