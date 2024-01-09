#!/usr/bin/python3
"""
This module defines a BaseGeometry class
"""


class BaseGeometry:
    """
    This class represents a BaseGeometry

    Methods:
    Area raises an exception
    integer_validator validates the value passed to it
    """

    def area(self):
        """
        Raises an Exception with a message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates value

        args:
            Name; name of value always a string
            Value: to be validated. must be an integer
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle
    and inherits from BaseGeometry

    Attributes:
        width - width of the rectangle
        height - height of the rectangle

    Methods:
    Instantiation with width and height
    """

    def __init__(self, width, height):
        """
        initializes the rectangle with width and height

        Args:
            width - width of the rectangle
            height - height of the rectangle
        """
        BaseGeometry.integer_validator("width", self.width)
        BaseGeometry.integer_validator("height", self.height)
        self.__width = width
        self.__height = height
