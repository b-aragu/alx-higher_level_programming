#!/usr/bin/python3

""" My list"""


class MyList(list):
    """ inherit from list """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
