#!/usr/bin/python3

""" Improve Geometry """


class BaseGeometry:
    """define class """
    def area(self):
        """define area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
        self.name = value
