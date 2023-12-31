#!/usr/bin/python3
"""Square module"""


class Square:
    """Represents a square

    Attributes:
        size: Size of a given square.

    Methods:
        area: Returning the current square area.
        size: Set and get the square's size.
        my_print: Prints the square using #.
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            result = "#" * self.__size
            for i in range(self.__size):
                print(result)
