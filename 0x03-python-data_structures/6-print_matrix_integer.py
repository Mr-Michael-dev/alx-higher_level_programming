#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers
    matrix: matrix to be printed
    """
    if matrix is None:
        print(None)
    for i in matrix:
        for j in i:
            print("{}".format(j), end=" ")
        print()
