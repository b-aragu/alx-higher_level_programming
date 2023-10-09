#!/usr/bin/python3
# 7-base_geometry.py

"""empty class base geometry"""


class BaseGeometry:
    """represent base geometry """
    def area(self):
        """"Not implemented. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates values"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
