#!/usr/bin/python3
# printing the number and list of its arrguement


if __name__ == "__main__":
    import sys
    elements = len(sys.argv)
    print("{} arguments".format(elements - 1))

    if elements > 1:
        i = 0
        for args in sys.argv[1:]:
            i += 1
            print("{}: {}".format(i, args))
