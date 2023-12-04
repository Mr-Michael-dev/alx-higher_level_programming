#!/usr/bin/python3

def max_integer(my_list=[]):
    """Returns the biggest integer of a list."""
    if my_list is None or len(my_list) == 0:
        return None
    else:
        new_list = sorted(my_list)
    return new_list[-1]
