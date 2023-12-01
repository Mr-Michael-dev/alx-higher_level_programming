#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    length = len(sys.argv)

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))

    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
	sys.exit(1)

    if length == 2:
        print("1 argument:")
        print("{}: {}".format(num, sys.argv[num]))
    else:
        print("{} arguments:".format(length - 1))
        for length in range(1, length):
            print("{}: {}".format(num, sys.argv[num]))
            num += 1
