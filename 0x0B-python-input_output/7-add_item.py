#!/usr/bin/python3
"""
    This module adds all arguments to a Python list,
    and then save them to a json file
"""


import sys
import os

load_json = __import__('6-load_from_json_file').load_from_json_file

save_json = __import__('5-save_to_json_file').save_to_json_file


args = sys.argv

# check number of arguments
if len(args) < 2:
    print("Error: Usage: {} <items to add>".format(args[0]), file=sys.stderr)
    exit()

filename = "add_item.json"
i = 1

# check if add_item.json exist and load it
if os.path.exists(filename):
    my_list = load_json(filename)
    while i < len(args):
        my_list.append(args[i])
        i += 1

    # save new list to add_item.json
    save_json(my_list, filename)
else:
    my_list = []
    # create a new list
    while i < len(args):
        my_list.append(args[1])
        i += 1
    # save to json file add_item.json
    save_json(my_list, filename)
