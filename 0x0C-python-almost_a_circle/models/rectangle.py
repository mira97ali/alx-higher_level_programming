#!/usr/bin/python3
"""Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Width Getter"""
        return self.__width

    @width.setter
    def width(self, new_width):
        """Width Setter"""
        self.__width = new_width

    @property
    def height(self):
        """Height Getter"""
        return self.__height

    @height.setter
    def height(self, new_height):
        """Height Setter"""
        self.__height = new_height

    @property
    def x(self):
        """X Getter"""
        return self.__x

    @x.setter
    def x(self, new_x):
        """X Setter"""
        self.__x = new_x

    @property
    def y(self):
        """Y Getter"""
        return self.__y

    @y.setter
    def y(self, new_y):
        """Y Setter"""
        self.__y = new_y
