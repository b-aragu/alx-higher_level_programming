#!/usr/bin/python3
# 1-safe_print_integer.py

"""Safe printing of an integer list"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
