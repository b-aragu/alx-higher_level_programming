#!/usr/bin/python3

"""class to JSON"""
import json


def class_to_json(obj):
    """
returns dict desription with simple data structure for Json serialization
args:
    obj - an instance of a class

    """
    return obj.__dict__
