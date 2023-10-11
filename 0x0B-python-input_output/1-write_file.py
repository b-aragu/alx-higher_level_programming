#!/usr/bin/python3
# 1-write_file.py

"""Write to a file"""


def write_file(filename="", text=""):
    """
 A function that writes a string to a text file(UTF8)
 args:
    filename - name of the file to be written to
    text - text to be written on the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f = f.write(text)
        return f
