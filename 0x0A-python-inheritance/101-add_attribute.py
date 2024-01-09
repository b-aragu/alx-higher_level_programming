#!/usr/bin/python3
"""can I?"""


def add_attribute(obj, attr, value):
    """add a new attribute to an bject if possible """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)

    if getattr(obj, attr) != value:
        raise TypeError("can't add new attribute")
