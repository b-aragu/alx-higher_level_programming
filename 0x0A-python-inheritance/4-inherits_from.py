#!/usr/bin/python3

""" only sub class of """


def inherits_from(obj, a_class):
    """ true otherwise false"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
