#!/usr/bin/python3
def no_c(my_string):
    for idx in range(0, len(my_string)):
        if my_string[idx] == "c" or my_string[idx] == "C":
            my_string[idx] = " "
    return my_string
