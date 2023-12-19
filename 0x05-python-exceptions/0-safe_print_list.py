#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """prints elements in a list

    args:
        my_list: the list to print
        x: the number of elements to print

    Returns:
        The actual number printed
    """

    ele_printed = 0
    try:
        for i, elements in enumerate(my_list):
            if i >= x:
                break
            print(elements, end="")
            ele_printed += 1
    except:
        pass

    print()
    return ele_printed
