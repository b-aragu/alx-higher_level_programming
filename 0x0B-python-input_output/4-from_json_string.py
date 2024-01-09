#!/usr/bin/python3
# 4-from_json_string.py

""" From JSON string to Object """
import json


def from_json_string(my_str):
    """
    return an object rep by json string
    args:
        my_str: object to be converted to json string
    """
    return json.loads(my_str)
