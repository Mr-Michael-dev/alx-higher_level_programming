#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a list
    my_list: list
    idx: index of element

    returns the element
    """
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        return my_list[idx]

