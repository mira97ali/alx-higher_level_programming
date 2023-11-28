#!/usr/bin/python3
def remove_char_at(string, n):
    result = ""
    for i in range(len(string)):
        if i != n:
            result += string[i]
    return result
