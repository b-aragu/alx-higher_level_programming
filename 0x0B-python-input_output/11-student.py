#!/usr/bin/python3
# 10-student.py

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

    def to_json(self, attrs=None):
        """get dict rep of student"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
