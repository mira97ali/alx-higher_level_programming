#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """My List"""
    def print_sorted(self):
        """print sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
