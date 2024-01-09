#!/usr/bin/python3
"""
This module defines a list
"""


class MyList(list):
    """
    MyList class inheriting the list class

    Methods:
    Instantiation method calling the superclass method
    print_sorted method prints the list in ascending order
    """

    def __init__(self):
        """
        Initializes the object

        calls the superclsss method on list
        """
        super().__init__()

    def print_sorted(self):
        """
        prints the list in ascending order
        """
        print(sorted(self))
