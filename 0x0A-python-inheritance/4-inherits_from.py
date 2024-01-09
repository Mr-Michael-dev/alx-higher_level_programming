#!/usr/bin/python3
"""
This module checks if an instance inherited from
a specified class
"""


def inherits_from(obj, a_class):
    """
    Returns true if is subclass otherwise false
    """
    if issubclass(obj, a_class):
        return True
    else:
        return False
