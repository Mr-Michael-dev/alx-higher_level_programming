#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    if matrix is None:
        print(None)
    elif not matrix:
        print("Empty matrix")
    else:
        for row in matrix:
            for num in row:
                print("{:d}".format(num), end=" ")
            print()
