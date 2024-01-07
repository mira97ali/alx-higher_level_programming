#!/usr/bin/python3
"""
Calculate the addition of numbers.
Functions:
    - add_integer(a, b): Add two int/float and returns the addition of a and b
"""


def add_integer(a, b=98):
    """Adding two integers
    a and b can be either int or float only, default value of 98 for b if not provided.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
