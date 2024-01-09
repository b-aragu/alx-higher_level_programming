#!/usr/bin/python3
# 9-student.py

""" student to JSON """


class Student:
    """
    defines a student
    """
    def __init__(self, first_name, last_name, age):
        """ instation of class student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve dict rep of Student instance"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {d: getattr(self, d) for d in attrs if hasattr(self, d)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all the attributes of the student instance """
        for k, v in json.items():
            setattr(self, k, v)
