#!/usr/bin/python3
"""
This module reads a text file and pront to stdout
"""


def read_file(filename=""):
    """
    opens a file, reads the file and print to stdout

    args:
        filename: the name of the file
    """

    with open(filename, encoding='utf-8') as file:
        print(file.read())
