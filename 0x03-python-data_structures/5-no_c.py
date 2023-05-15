#!/usr/bin/python3
# 5-no_c.py

"""can you c me now"""


def no_c(my_string):
    new_string = [s for s in my_string if s != 'c' and s != 'C']
    return("".join(new_string))
