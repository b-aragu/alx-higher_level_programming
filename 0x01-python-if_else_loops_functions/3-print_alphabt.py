#!/usr/bin/python3
# 2-print_alphabet.py

for i in range(97, 123):
    if chr(i) == 'q' or chr(i) == 'e':
        continue
    print("{}".format(chr(i)), end="")
