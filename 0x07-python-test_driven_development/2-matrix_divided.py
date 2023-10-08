#!/usr/bin/python3
# matrix_divided.py

"""function to divide a matrix """


def matrix_divided(matrix, div):
    """
divides all element of a matrix
args:
    matrix - a list of int or float and of the same size
    div - a number or a float
raises:
    TypeError - if matrix div aint inegers or floats
    ZeroDivisionError - if div is 0
return:
    a new matrix
    """
    o = "matrix must be a matrix (list of lists) of integers/floats"
    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError(o)
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in row] for row in matrix]
