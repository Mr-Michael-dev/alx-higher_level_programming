#!/usr/bin/python3

"""
prints the last digit of random numbers
and check if 0, less than 6 or greater than 5
"""

import random
number = random.randint(-10000, 10000)

if number < 0:
    l_digit = number % -10
else:
    l_digit = number % 10

if l_digit == 0:
    print(f'Last digit of {number} is {l_digit} and is 0')
elif l_digit < 6 and l_digit != 0:
    print(f'Last digit of {number} is {l_digit} and is less than 6 and not 0')
else:
    print(f'Last digit of {number} is {l_digit} and is greater than 5')
