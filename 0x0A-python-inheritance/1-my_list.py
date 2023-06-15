#!/usr/bin/python3
# 1-my_list.py
"""for  an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing forbuilt-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
