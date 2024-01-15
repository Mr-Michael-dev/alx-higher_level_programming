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
        int_validator(name, value): Validates if the value is an integer > 0
        x_and_y_validator(name, value): Validates if the value is an int >= 0
    """

    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def int_validator(self, name, value):
        """
        Checks if the value inputted is an integer and > 0

        Args:
            name (str): name of the value to check
            value: value to be checked

        Raises:
            TypeError: if not an integer
            Value Error: if value <= 0
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def x_and_y_validator(self, name, value):
        """
        Checks if the value inputted is an integer and >= 0

        Args:
            name (str): name of the value to check
            value: value to be checked

        Raises:
            TypeError: if not an integer
            Value Error: if value < 0
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation method. Calls the super class with id.

        Args:
            width: width of the rectangle
            height: height of the rectangle
            x (int): x-cordinate
            y (int): y-cordinate
            id: id of the rectangle
        """

        super().__init__(id)
        self.int_validator("width", width)
        self.int_validator("height", height)
        self.x_and_y_validator("x", x)
        self.x_and_y_validator("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.int_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.int_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.x_and_y_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.x_and_y_validator("y", value)
        self.__y = value

    def area(self):
        """
        computes the area of Rectangle

        Returns:
            The product of width and height
        """
        return (self.width * self.height)
