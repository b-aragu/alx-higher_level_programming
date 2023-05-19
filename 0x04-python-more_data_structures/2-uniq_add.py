#!/usr/bin/python3
# 2-uniq_add.py

"""unique addition"""


def uniq_add(my_list=[]):
    result = 0
    duplicated = list(set(my_list))
    for item in duplicated:
        result += item
    return result
