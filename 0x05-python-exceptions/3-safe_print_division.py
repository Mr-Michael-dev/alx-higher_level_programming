#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        result = None
    finally:
        if result is not None:
            print("Inside result: {}".format(result))
        else:
            print("Inside result: {}".format(result))
        return result
