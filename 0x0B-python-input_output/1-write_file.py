#!/usr/bin/python3
# 1-write_file.py
""" Write to a file """


def write_file(filename="", text=""):
    """
    A function that writes to a text file and returns no of characters written
    args:
        filename: name of the file
        text: data being written to the file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return f.tell()
