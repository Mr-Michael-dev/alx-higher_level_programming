#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """prints all integers of a list
    assuming the list only contains integers
    """
    for integers in my_list:
        print("{:d}".format(integers))
