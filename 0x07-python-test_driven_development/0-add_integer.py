#!/usr/bin/python3
"""
This module adds two integers
a: First integer
b: Second integer
"""


def add_integer(a, b=98):
    """
    Returns the sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
