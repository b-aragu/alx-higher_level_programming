#!/usr/bin/python3
# 12-roman_to_int.py

"""convert roman integers to numerals"""


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0
    previous_value = 0

    for char in roman_string:
        value = roman_numerals.get(char, 0)
        if value > previous_value:
            result += value - 2 * previous_value
        else:
            result += value
        previous_value = value

    return result
