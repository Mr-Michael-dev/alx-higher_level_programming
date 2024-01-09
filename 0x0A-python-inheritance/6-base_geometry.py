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
