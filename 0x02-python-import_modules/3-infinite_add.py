#!/usr/bin/python3
import sys
if __name__ == "__main__":
    numbers = sys.argv[1:]
    result = 0
    for number in numbers:
        result = result + int(number)
    print((result))
