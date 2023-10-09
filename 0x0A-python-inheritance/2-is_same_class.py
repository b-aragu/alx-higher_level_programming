#!/usr/bin/python3
# 2-is_same_object.py

"""Exact same object"""


def is_same_class(obj, a_class):
    """
    args:
        obj, a_class
    return:
        True if obj is exactly an instance of specified class
    """
    if type(obj) == a_class:
        return True
    return False
