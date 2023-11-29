#!/usr/bin/python3

"""
the function prints the last digit of a number
"""


def print_last_digit(number):

    last_digit = abs(number) % 10

    print('{:d}'.format(last_digit), end="")

    return last_digit
