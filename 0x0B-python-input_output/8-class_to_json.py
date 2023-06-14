#!/usr/bin/python3
# 8-class_to_json.py

"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dict representation of a simple data structure."""
    return obj.__dict__
