#!/usr/bin/python3
# 11-delete_at.py

"""delete an item at a specific position"""


def delete_at(my_list=[], idx=0):
    if not my_list[idx] or idx < 0:
        return my_list
    del my_list[idx]
    return my_list
