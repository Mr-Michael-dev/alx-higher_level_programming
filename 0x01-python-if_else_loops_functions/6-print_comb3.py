#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        print("{:d}".format(i), end="")
        print("{:d}".format(j), end=", "if not (i == 8 and j == 9) else "\n")
