#!/usr/bin/python3
# 6-print_matrix_integer.py

"""Lists a list = matrix"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            if row[len(row) - 1] == element:
                print("{}".format(row[len(row) - 1]), end="")
            else:
                print("{}".format(element), end=" ")
        print()
