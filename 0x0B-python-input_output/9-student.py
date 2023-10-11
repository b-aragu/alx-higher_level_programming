#!/usr/bin/python3
# 9-student.py

"""student to json"""


class Student:
    """
defines a student by:

Public instance attributes:
    first_name
    last_name
    age
Instantiation : def __init__(self, first_name, last_name, age):
Public method def to_json(self):that retrieve a dict repr of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """get dict rep of student"""
        return self.__dict__
