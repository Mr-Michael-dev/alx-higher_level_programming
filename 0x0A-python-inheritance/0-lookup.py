#!/usr/bin/python3
"""
This module looksup the list of available methods
and attributes in an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes
    and methods of an object
    """
    return dir(obj)
