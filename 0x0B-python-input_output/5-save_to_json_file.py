#!/usr/bin/python3
# 5-save_to_json_file.py

"""save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """
function that writes an object to a text file using JSON rep
args:
    my_obj - object to be written to the .txt file
    filename - name of the .txt file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
