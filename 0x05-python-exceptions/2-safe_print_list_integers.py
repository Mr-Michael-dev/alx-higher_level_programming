#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints first x integers in a list, skips non-integers silently.

    Args:
    my_list: The list to print.
    x: The number of elements to access.

    Returns:
    The actual number of integers printed.
    """
    int_printed = 0
    try:
        for i, element in enumerate(my_list):
            if i >= x:
                break
            try:
                print("{:d}".format(element), end="")
                int_printed += 1
            except ValueError:
                pass
    finally:
        print()
        return int_printed
