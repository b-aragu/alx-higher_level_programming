#!/usr/bin/python3
# 5-print_comb2.py

for i in range(100):
    print("{:02d}".format(i), end=", " if i < 99 else "\n")
