#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys
    assuming that all keys are strings,
    Keys should be sorted by alphabetic order
    """
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
