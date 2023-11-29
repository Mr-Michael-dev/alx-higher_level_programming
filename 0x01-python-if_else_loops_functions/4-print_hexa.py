#!/usr/bin/python3

"""
prints number from 0 to 99 in decimal and hexadecimal
"""

for i in range(99):
    print("{:d} = 0x{:x}".format(i, i))
