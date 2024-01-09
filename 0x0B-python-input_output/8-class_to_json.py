#!/usr/bin/python3
# 8-class_to_json.py

""" class to JSON """


def class_to_json(obj):
    """
    Returns the dict description with simple data structure
    args:
        obj: an instance to a class
    """
    return obj.__dict__
