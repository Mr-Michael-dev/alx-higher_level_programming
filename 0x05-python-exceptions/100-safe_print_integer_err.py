#!/usr/bin/python3

def safe_print_integer_err(value):

    """prints and integer with {:d} format specifier

    args:
        value: value to be printed

    Returns: True if printed or False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err))
        return False
