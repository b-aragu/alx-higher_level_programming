#!/usr/bin/python3

""" inherits from rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class for a square object """

    def __init__(self, size):
        """instantiation """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
