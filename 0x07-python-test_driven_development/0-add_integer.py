#!/usr/bin/python3
# 0-add_integer.py

"""Integer addition"""
def add_integer(a, b=98):
    """Returns integer addition of a and b 
    float arguement are typecasted to int before addition is perfomed
    Raises:
        TypeError: if either of a and b is no integer or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
