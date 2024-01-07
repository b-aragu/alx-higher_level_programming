#!/usr/bin/python3

""" Text indentation """

def text_indentation(text):
    """ prints a text with 2 new lines after each of the character ., ?, :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    char = [".", "?", ":"]
    for i in text:
        print(i, end="")
        if i in char:
            print()
            print()
            continue
