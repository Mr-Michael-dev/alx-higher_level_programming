#!/usr/bin/python3
"""
This module checks if object is an instance
or subclass of a class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns true if is instance or subclass otherwise false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
