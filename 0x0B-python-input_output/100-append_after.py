#!/usr/bin/python3
"""
This module inserts a lime of text inbetween a text file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line
    containing a specific string

    Args:
        filename: the name of the file
        search_string: the specific string to search for in each line
        new_string: the line of text to insert after each line
                    containing the search string
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
