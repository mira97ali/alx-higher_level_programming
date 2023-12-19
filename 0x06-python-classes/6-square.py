#!/usr/bin/python3
"""Square module"""


class Square:
    """Represents a square

    Attributes:
        size: Size of a given square.
        position: Position given.

    Methods:
        area: Returning the current square area.
        size: Set and get the square's size.
        my_print: Prints the square using #.
        position: Set/Get the position.
    """

    def __init__(self, size=0, position=(0, 0)):
        # Init Size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        # Init Position
        position_error = "position must be a tuple of 2 positive integers"
        if not isinstance(position, tuple):
            raise TypeError(position_error)
        if len(position) != 2:
            raise TypeError(position_error)
        for i in position:
            if not isinstance(i, int) or i < 0:
                raise TypeError(position_error)
        self.__position = position

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
            prefix = " " * self.__position[0]
            line = prefix + "#" * self.__size
            for i in range(self.__position[1]):
                print("")
            for j in range(self.__size):
                print(line)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        error = "position must be a tuple of 2 positive integers"
        if not isinstance(value, tuple):
            raise TypeError(error)
        if len(value) != 2:
            raise TypeError(error)
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError(error)
        self.__position = value
