#!/usr/bin/python3

"""
prints the ASCII alphabet, in reverse order,
alternating lowercase and uppercase
(z in lowercase and Y in uppercase),
not followed by a new line.
"""

for i in range(90, 64, -1):
    if i % 2 == 0:
        i += 32
    print("{}".format(chr(i)), end="")
