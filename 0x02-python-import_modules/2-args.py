#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = (len(sys.argv) - 1)
    if result == 0:
        print("{} arguments.".format(result))
    else:
        if result == 1:
            print("{} argument:".format(result))
        else:
            print("{} arguments:".format(result))
        for i in range(1, result+1):
            print("{}: {}".format(i, sys.argv[i]))
