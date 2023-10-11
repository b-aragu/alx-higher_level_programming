#!/usr/bin/python3
# 4-from_json_string.py

"""from JSON string to Object"""
import json


def from_json_string(my_str):
    """
function that returns an object(python data structure ) from JSON
args:
    my_str - object to decode
    """
    return json.loads(my_str)
