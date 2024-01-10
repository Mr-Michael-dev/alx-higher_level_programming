#!/usr/bin/python3
"""
This module apends to a text file
"""


def append_write(filename="", text=""):
    """
    opens and appends to a file

    args:
        filename: the name of the file
        text: the text to append in the file

    Returns: the number of characters
    """

    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
