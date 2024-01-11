#!/usr/bin/python3
"""
this module adds new attr to a class if possible
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        - obj: Object to which the attribute should be added
        - name: Name of the new attribute
        - value: Value of the new attribute

    Raises:
        - TypeError: If the object can't have a new attribute
    """
    if not hasattr(obj, "__dict__") and not hasattr(obj, "__slots__"):
        raise TypeError("can't add new attribute")
    
    setattr(obj, name, value)
