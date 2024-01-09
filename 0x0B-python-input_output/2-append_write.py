#!/usr/bin/python3
# 2-append_write.py

""" Append to a file """


def append_write(filename="", text=""):
    """
        Function that appends string to end of the file
        args:
            filename: name of the file
            string: data to be appended to file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
