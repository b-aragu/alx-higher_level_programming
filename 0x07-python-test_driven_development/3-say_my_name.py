#!/usr/bin/python3
# 3-say_my_name.py

"""say my name """


def say_my_name(first_name, last_name=""):
    """
    function that prints My name is <first name > <last name>
    args:
        first_name - string
        last_name - string
    raises:
        TypeError - if fisrst and last name arent strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
