#!/usr/bin/python3
# 0-read_file.py

"""text file reading function"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, encoding="utf-8") as f:
        return f.write("text")
baragu@baragu254:~/Documents/ALx/
