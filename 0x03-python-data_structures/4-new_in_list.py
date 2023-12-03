#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element at position in a list without modifying list
    my_list: list
    idx: index of element
    element: element to replace

    returns  copy of list
    """

    new_list = my_list.copy()
    if new_list is None or idx < 0 or idx >= len(new_list):
        return new_list
    else:
        new_list[idx] = element
        return new_list
