#!/usr/bin/python3

""" inverter """


class MyInt(int):
    """ a class for a rebellious integer"""

    def __eq__(self, other):
        """ override the == """
        return super().__ne__(other)

    def __ne__(self, other):
        """ override the != """
        return super().__eq__(other)
