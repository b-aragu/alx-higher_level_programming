#!/usr/bin/python3
# 4-inherits_from.py


def inherits_from(obj, a_class):
    """
function that return true if obj is instance of class inherited
args:
    obj - object to be checked
    a_class - class to be checked against
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
