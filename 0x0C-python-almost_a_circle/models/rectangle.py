#!/usr/bin/python3
# rectangle.py

""" Rectangle model that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """Rectangle model that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for width """
        self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x """
        self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y """
        self.__y = value
