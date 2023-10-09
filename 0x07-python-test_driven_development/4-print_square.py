#!/usr/bin/python3
# 4-print_square.py

"""print square"""


def print_square(size):
    """
    A    function that priints a square with character '#'
    args:
        size - the length of the square
    raises:
        TypeError - if size aint int
        ValueError - if size is less than 0
        TypeError - if size is float and less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:

        raise TypeError("size must be an integer")
    for i in range(size):
        print('#' * size)
