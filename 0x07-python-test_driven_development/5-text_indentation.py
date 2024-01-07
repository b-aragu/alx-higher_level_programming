#!/usr/bin/python3

""" Text indentation """

def text_indentation(text):
    """ prints a text with 2 new lines after each of the character ., ?, :"""
    buff = ""
    split = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i in ".?:":
            buff += i + '\n\n'
        else:
            buff += i

    split = buff.split('\n')
    for letter in split:
        print(letter.strip())
