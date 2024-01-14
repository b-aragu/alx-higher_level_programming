#!/usr/bin/python3
# square.py

""" Defines a square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class that inherits from rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize the rectangle class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns a string representation of the square """
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}"\
               f" - {self.width}"

    @property
    def size(self):
        """ Getter for size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size attribute """
        self.width = value
        self.height = value
