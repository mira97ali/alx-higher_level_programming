#!/usr/bin/python3
"""Square module"""


class Square:
    """Represents a square

    Attributes:
        size: Size of a given square.

    Methods:
        area: Returning the current square area.
        size: Set and get the square's size.
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    def size(self):
        return self.__size
    
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
