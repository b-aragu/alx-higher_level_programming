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

    def to_json(self):
        """retrieve dict rep of Student instance"""
        return self.__dict__
