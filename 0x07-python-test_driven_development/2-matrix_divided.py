#!/usr/bin/python3

"""Divide a matrix"""


def matrix_divided(matrix, div):
    """ divides all element of a matrix """
    if not (
    isinstance(matrix, list) and 
    matrix and  # Ensure matrix is not an empty list
    all(isinstance(row, list) for row in matrix) and
    all(isinstance(ele, (int, float)) for ele in [num for row in matrix for num in row])
):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int)  and not isinstance(div , float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [[round(element / div, 2)for element in row] for row in matrix]

    return new
