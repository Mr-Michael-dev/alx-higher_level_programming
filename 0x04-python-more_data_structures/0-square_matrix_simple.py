#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix
    """
    new_matrix = []
    for row in matrix:
        sq_row = list(map((lambda x: x**2), row))
        new_matrix.append(sq_row)
    return new_matrix
