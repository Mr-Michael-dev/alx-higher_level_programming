#!/usr/bin/python3
"""
This module checks if object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Returns true if is instance otherwise false
    """
    if type(obj) is a_class:
        return True
    else:
        return False
