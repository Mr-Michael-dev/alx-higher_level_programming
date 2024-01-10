#!/usr/bin/python3
"""
This module returns the JSON representation of an object
"""


def to_json_string(my_obj):
    """
    Serializes an object

    args:
        my_obj: object to be serialized

    Return: The JSON representation
    """
    import json

    return json.dumps(my_obj)
