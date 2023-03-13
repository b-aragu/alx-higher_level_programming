#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for z in my_string:
        if z == 'C' or z == 'c':
            continue
        result += z
    return result
