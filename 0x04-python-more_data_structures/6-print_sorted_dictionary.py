#!/usr/bin/python3
# 6-print_sorted_dictionary.py

"""print sorted dictionary"""


def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())

    for key in sorted_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
