#!/usr/bin/python3
# infinite addition of integers


if __name__ == "__main__":
    import sys
    summ = 0
    for args in sys.argv[1:]:
        summ += int(args)
    print(summ)
