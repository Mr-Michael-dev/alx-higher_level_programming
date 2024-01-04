#!/usr/bin/python3

"""
    This module defines a rectangle.
"""


class Rectangle:
    """
    This class represents a rectangle with the attrubutes.

    width: the width of the rectangle
    height: the height of the rectangle

    It has an instantiation method with optional width and height
    """
    def __init__(self, width=0, height=0):
        """
        Instantiates with optional width and height

        width: the width of the rectangle
        height: the height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        gets the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of the rectangle
        """
        if not int(value):
            raise TypeError(width must be an integer)
        elif value < 0:
            raise ValueError(width must be >= 0)
        else:
            self.__width = value

    @property
    def height(self):
        """
        gets the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height of the rectangle
        """
        if not int(value):
            raise TypeError(height must be an integer)
        elif value < 0:
            raise ValueError(height must be >= 0)
        else:
            self.__height = value
