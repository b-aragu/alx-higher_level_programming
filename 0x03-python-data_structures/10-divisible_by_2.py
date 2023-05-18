#!/usr/bin/python3
# 10-divisible_by_2.py

"""Only by 2"""


def divisible_by_2(my_list=[]):
    new_list = []
    for item in my_list:
        if item % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
