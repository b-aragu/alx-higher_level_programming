#!/usr/bin/python3
# 10-best_score.py

"""Best score"""


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    largest_key = max(a_dictionary, key=a_dictionary.get)
    return largest_key
