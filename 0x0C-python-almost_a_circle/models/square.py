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

    def to_dictionary(self):
        """ Return dict representation of square """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    @property
    def size(self):
        """ Getter for size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size attribute """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates attribute """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.size = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        else:
            for key, item in kwargs.items():
                if key == "id":
                    self.id = item
                elif key == "size":
                    self.size = item
                elif key == "x":
                    self.x = item
                elif key == "y":
                    self.y = item
