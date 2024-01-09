#!/usr/bin/python3
# 6-load_from_json_file.py

""" Create object from a JSON file """
import json


def load_from_json_file(filename):
    """
    A function that creates object from a json file
    args:
        name of the json file
    """
    with open(filename) as f:
        return json.load(f)
