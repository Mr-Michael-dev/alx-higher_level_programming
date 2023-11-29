#!/usr/bin/python3

"""
the function prints the last digit of a number
"""


def print_last_digit(number):

    if number < 0:
        last_digit = number % -10
    else:
        last_digit = number % 10

    print('{:d}'.format(last_digit), end="")
    return last_digit
