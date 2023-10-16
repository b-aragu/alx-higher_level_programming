#!/usr/bin/python3

# base.py

"""base class"""


class Base:
    """a base class
private atributes:
        __nb_objects
class constructor:
    def __init__(self, id=none)
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """the class constructor"""
        if id is not None:
            self.id = id
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
