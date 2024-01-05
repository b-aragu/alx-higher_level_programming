#!/usr/bin/python3

""" Low memory cost """


class LockedClass:
    """no attribute can be created if it doesnt have first name"""
    __slots__ = ('first_name',)
