#!/usr/bin/python3
# 0-print_list_integer.py

"""Prints a list of integer"""


def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
