#!/usr/bin/python3
# 0-square_matrix_simple.py

"""squared simple"""


def square_matrix_simple(matrix=[]):
    squared = [[x ** 2 for x in row] for row in matrix]
    return squared
