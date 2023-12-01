#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num = 1
    length = len(sys.argv)

    if length == 1:
        print("0 argument.")
    elif length == 2:
        print("1 argument:")
        print("{}: {}".format(num, sys.argv[num]))
    else:
        print("{} arguments:".format(length - 1))
        for length in range(1, length):
            print("{}: {}".format(num, sys.argv[num]))
            num += 1
