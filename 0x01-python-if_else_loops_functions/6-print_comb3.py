#!/usr/bin/python3
# 6-print_comb3.py

for i in range(9):
    for x in range((i + 1), 10):
        if i != x:
            print("{}{}".format(i, x), end=", " if i < 8 else "\n")
