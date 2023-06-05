#!/usr/bin/python3
# 2-safe_print_list_integers.py

"""Print and count integers"""


def safe_print_list_integers(my_list=[], x=0):
    """prints the first x element of a list and only integer"""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
