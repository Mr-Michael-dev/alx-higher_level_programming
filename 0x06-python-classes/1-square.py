#!/usr/bin/python3

"""
    This module defines a square.
"""


class Square:
    """
    This class represents a square with an attribute for:

    -size: the size of the square

    It has an instantiation method without any type/value verification
    """

    def __init__(self, size):
        """
        This is the init method

        it initializes the object specified with size
        """
        self.__size = size
