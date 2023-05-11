#!/usr/bin/python3
# 100-my_calculator.py

if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys
    operators = {"+": add, "-": sub, "*": mul, "/": div}

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    k = sys.argv[2]

    if k not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a, b = int(sys.argv[1]), int(sys.argv[3])
    print("{} {} {} = {}".format(a, k, b, operators[k](a, b)))
