#!/usr/bin/python3
"""
This module writes to a text file
"""


def write_file(filename="", text=""):
    """
    opens and write to a file

    args:
        filename: the name of the file
        text: the text to write in the file

    Returns: the number of characters
    """

    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
