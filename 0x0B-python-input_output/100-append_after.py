#!/usr/bin/python3
# 100-append_after.py

""" Search and update """


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file after each line contaiing string
    args:
        filename: name of file
        search_string: string being searched 
        new_string: string to replace the search string
    """
    with open(filename, 'r', encoding="utf-8") as f:
        text = f.readlines()

    with open(filename, 'w', encoding="utf-8") as f:
        for line in text:
            if search_string in line:
                line = line.replace(search_string, new_string + '\n')
            f.write(line)
