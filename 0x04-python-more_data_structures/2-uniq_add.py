#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds all unique integers in a list 
    (only once for each integer)
    """
    unique_num = set(my_list)
    return sum(unique_num)
