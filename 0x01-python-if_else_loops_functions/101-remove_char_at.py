#!/usr/bin/python3

"""
creates a copy of the string,
removing the character at the position n
"""


def remove_char_at(str, n):
    string_cpy = ""

    for i in range(len(str)):
        if i != n:
            string_cpy += str[i]
    return string_cpy
