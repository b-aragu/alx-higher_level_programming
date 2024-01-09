#!/usr/bin/python3
# 3-to_json_string.py
import json

""" To Json string"""


def to_json_string(my_obj):
    """
    returns the json string rep of an object (string)
    args:
        my_obj: the object to be serialized
    """
    return json.dumps(my_obj)
