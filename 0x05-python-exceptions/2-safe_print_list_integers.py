#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    number = 0
    for i in range(x):
        try:
            try:
                result = "{:d}".format(my_list[i])
            except (ValueError, TypeError):
                continue
            print(result, end="")
            number = number + 1
        except IndexError:
            break
    print("\n", end="")
    return number
