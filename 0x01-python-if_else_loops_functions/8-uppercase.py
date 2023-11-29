#!/usr/bin/python3

"""
prints a string in upper case
"""


def uppercase(str):
    string = ""
    for i in str:
        if ord(i) in range(97, 123):
            string += chr(ord(i) - 32)
        else:
            string += i
    print("{}".format(string))
