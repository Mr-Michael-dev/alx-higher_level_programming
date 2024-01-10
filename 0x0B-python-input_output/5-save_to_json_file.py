#!/usr/bin/python3
"""
This module writes an object to a text file
using JSON representation
"""


def save_to_json_file(my_obj, filename):
    """
    opens and write a serialized object to a file

    args:
        my_obj: object to serialize
        filename: the name of the file
    """

    import json

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
