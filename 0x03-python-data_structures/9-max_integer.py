#!/usr/bin/python3
# 9-max_integer.py

"""find the biggest integer"""


def max_integer(my_list=[]):
    if not my_list:
        return None

    for i in range(len(my_list) - 1):
        if my_list[i] < my_list[i + 1]:
            temp = my_list[i + 1]
            my_list[i + 1] = my_list[i]
            my_list[i] = temp

    return my_list[0]
