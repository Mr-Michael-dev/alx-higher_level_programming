#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a list
    my_list: list
    idx: index of element

    returns the element
    """
    if my_list is None or idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
