#!/usr/bin/python3
"""
This module provides function for working with JSON files
"""


import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file

    Args:
        filename: the name of the file containing JSON data

    Returns:
        The deserialized object
    """
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
