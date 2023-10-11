#!/usr/bin/python3
# 0-read_file.py

"""read file"""


def read_file(filename=""):
    """
function that reads a text file (UTF8) and prints it to stdout
args:
    filename - name of the file
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
