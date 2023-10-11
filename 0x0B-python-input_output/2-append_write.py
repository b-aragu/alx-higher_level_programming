#!/usr/bin/python3
# 2-append_write.py

""" appending to a file """


def append_write(filename="", text=""):
    """
A function that appends a string at the end of a text file (UTF8)
    args:
        filename (str) - name of the file
        text (str) - text to be added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f = f.write(text)
        return f
