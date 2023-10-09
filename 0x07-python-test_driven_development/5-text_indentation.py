#!/usr/bin/python3
# 5-text_indentation.py

"""
text indentation
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_paragraph = True

    for char in text:
        if char in '.?:':
            print(char, end='')
            new_paragraph = True
        else:
            if new_paragraph and char != ' ':
                print('\n\n', char, sep='', end='')
                new_paragraph = False
            else:
                print(char, end='')
