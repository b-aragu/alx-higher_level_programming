#!/usr/bin/python3
# 7-update_dictionary.py

"""update dictionary"""


def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    a_dictionary[key] = value
    return a_dictionary
