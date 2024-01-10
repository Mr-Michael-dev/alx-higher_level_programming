#!/usr/bin/python3
"""
This module returns object (python data structure
represented by a json string
"""


def from_json_string(my_str):
    """
    deserializes a json string

    args:
        my_str: string to be deserialized

    Return: The object data structure
    """
    import json

    return json.loads(my_str)
