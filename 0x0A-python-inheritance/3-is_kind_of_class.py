#!/usr/bin/python3
# 3-is_kind_of_class.py

"""same class or inherit"""


def is_kind_of_class(obj, a_class):
    """
    args:
        obj - the object
        a_class - the clas to check
    returns:
        True if object is instance of class inherited from 
    """
    if isinstance(obj , a_class):
        return True
    return False
