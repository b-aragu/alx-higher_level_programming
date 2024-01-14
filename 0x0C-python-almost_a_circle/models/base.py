#!/usr/bin/python3
# models.py

"""Defines a base class for all models in our hbnb clone"""


class Base:
    """Base class for all models in the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize the base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
