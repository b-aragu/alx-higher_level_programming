#!/usr/bin/python3
# 7-islower.py

def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()
