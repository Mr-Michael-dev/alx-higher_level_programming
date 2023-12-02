#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Rplaces an element at position in a list
    my_list: list
    idx: index of element
    element: element to replace

    returns list
    """
    if my_list is None or idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
