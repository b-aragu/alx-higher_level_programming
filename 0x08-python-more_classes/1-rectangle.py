#!/usr/bin/python3

"""Write an empty class Rectangle that defines a rectangle:"""


class Rectangle:
    """Write an empty class Rectangle that defines a rectangle:"""
    def __init__(self, width=0, height=0):
        """the init of class rectangle """
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

