#!/usr/bin/python3
# 7-add_tuple.py

"""addition of two tuples"""


def add_tuple(tuple_a=(), tuple_b=()):
    # Handle empty tuples
    if not tuple_a:
        tuple_a = (0, 0)
    if not tuple_b:
        tuple_b = (0, 0)

    # Handle tuples with less than 2 elements
    if len(tuple_a) < 2:
        tuple_a = (tuple_a[0], 0)
    if len(tuple_b) < 2:
        tuple_b = (tuple_b[0], 0)

    # Handle empty string elements
    if tuple_a[0] == '':
        tuple_a = (0, tuple_a[1])
    if tuple_a[1] == '':
        tuple_a = (tuple_a[0], 0)
    if tuple_b[0] == '':
        tuple_b = (0, tuple_b[1])
    if tuple_b[1] == '':
        tuple_b = (tuple_b[0], 0)
        # Perform tuple addition
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
