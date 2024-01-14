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

    def __str__(self):
        """Override to return [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__x}/"\
               f"{self.__y} - {self.__width}/{self.__height}"

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for width """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height  must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Return the area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """ Print in stdout the rectangle instance with the character # """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)
