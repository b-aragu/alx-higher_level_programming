#!/usr/bin/python3
# 0-add_integer.py

"""
integers addition
"""


def add_integer(a, b=98):
    """
    a function that adds integers
    args:
        a , b both int or float
    return:
        a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (a + b)
