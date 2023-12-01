#!/usr/bin/python3
import sys

if __name__ == "__main__":
    _sum = 0
    num = 1
    length = len(sys.argv)

    if length == 1:
        print("{}".format(_sum))
    else:
        for length in range(1, length):
            _sum += int(sys.argv[num])
            num += 1
        print("{}".format(_sum))
