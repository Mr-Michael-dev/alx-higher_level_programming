#!/usr/bin/python3
"""
This module represents rectangle class which is a subclass of Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from base.

    Attributes:
        __width -> width
        __height -> height
        __x -> x
        __y -> y

    Methods:
        __init__(): instantiation method
    """

    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation method. Calls the super class with id.

        Args:
            width: width of the rectangle
            height: height of the rectangle
            x:
            y:
            id: id of the rectangle
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
