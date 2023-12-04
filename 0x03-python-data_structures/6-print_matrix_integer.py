#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers"""
    if matrix is None:
        print(None)
    else:
        for row in matrix:
            for num in row:
                print("{:d}".format(j), end=" ")
            print()
