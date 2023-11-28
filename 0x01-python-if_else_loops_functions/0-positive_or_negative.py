#!/usr/bin/python3

"""
prints random number and indicates
if positive, negative or zero
"""
import random
number = random.randint(-10, 10)

if number > 0:
    print(f'{number} is positive')
elif number < 0:
    print(f'{number} is negative')
else:
    print(f'{number} is zero')
