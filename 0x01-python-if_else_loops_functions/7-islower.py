#!/usr/bin/python3

"""
checks if an alphabeth is lower case or upper case
"""


def islower(c):
    if ord(c) not in range(97, 123):
        return False
    else:
        return True
