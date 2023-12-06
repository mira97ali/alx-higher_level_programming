#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for key, value in enumerate(my_list):
        if value == search:
            my_list[key] = replace
    return my_list
