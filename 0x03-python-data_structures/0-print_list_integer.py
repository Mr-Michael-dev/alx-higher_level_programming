#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """prints all integers of a list
    assuming the list only contains integers
    """

    for i in range(len(my_list)):
        print("{}".format(my_list[i]))
