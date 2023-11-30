#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = sys.argv[1]
        b = sys.argv[3]
        operator = sys.argv[2]
        if operator not in "+-*/":
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        a = int(a)
        b = int(b)
        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = sub(a, b)
        elif operator == "/":
            result = div(a, b)
        else:
            result = mul(a, b)
        print("{} {} {} = {}".format(a, operator, b, result))
