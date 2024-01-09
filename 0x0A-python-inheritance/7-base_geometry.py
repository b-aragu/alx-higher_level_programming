#!/usr/bin/python3

""" Improve Geometry """


class BaseGeometry:
    """define class """
    def area(self):
        """define area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates an int """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = value
