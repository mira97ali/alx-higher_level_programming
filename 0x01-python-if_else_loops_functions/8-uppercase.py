#!/usr/bin/python3
def uppercase(string):
    result = ""
    for char in string:
        result += chr(ord(char) - 32) if 'a' <= char <= 'z' else char
    print("{}".format(result))
