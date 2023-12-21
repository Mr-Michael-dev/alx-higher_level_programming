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
    my_print method to print the square
    """

    def __init__(self, size=0, position=(0, 0)):
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

        if isinstance(position, tuple) and len(position) == 2:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Calculates the area of the square

        Returns:
        the current square area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        gets the size attribute
        """
        return self.__size

    @property
    def position(self):
        """
        gets the position attribute
        """
        return self.__position

    @size.setter
    def size(self, value):
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

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        Prints the square with the character # and considers the position.
        If size is equal to 0, print an empty line.
        If position[1] is greater than 0, add empty lines before printing.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
