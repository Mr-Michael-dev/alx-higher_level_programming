#!/usr/bin/python3

"""
This module defines a square.
"""


class Square:
    """
    This class represents a square with a private instance attribute:

    - size: the size of the square

    Methods:
    Instantiation method with type/value verification.
    Area method which returns area of square
    Size method to access the private attribute __size
    Size method to set the private attribute with verification
    """

    def __init__(self, size=0):
        """
        Initializes the object with the specified size.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of the square

        Returns:
        the current square area
        """
        return self.__size * self.__size

    def get_size(self):
        """
        gets the size attribute
        """
        return self.__size

    def set_size(self, value):
        """
        Sets the value of private attribute

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
