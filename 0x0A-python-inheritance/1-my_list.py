#!/usr/bin/python3
# 1-my_list.py


class MyList(list):
    """
    class that inherits from list
    methods:
        def print_sorted(self)
    """
    def print_sorted(self):
        """print a list in a sorted ascending order."""
        print(sorted(self))
