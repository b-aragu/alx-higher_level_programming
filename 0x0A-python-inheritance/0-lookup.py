#!/usr/bin/python3
# 0-lookup.py

"""lookup"""


def lookup(obj):
    """
a function that returns the list of available attributes and methods of an obj
returns:
    a list object
    """
    return (dir(obj))
