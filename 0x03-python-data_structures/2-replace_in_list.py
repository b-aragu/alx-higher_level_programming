#!/usr/bin/python3
# 2-replace_in_list.py

"""Replaces an elements"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list
