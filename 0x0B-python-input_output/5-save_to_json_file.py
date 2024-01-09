#!/usr/bin/python3
# 5-save_to_json_file.py

"""save object to file """
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an object to a text file using a JSON rep
    args:
        my_obj: obj to be saved to file
        filename: name of the file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
