#!/usr/bin/python3
"""Square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size Getter"""
        return super().width

    @size.setter
    def size(self, new_size):
        """size Setter"""
        super(self.__class__, type(self)).width.fset(self, new_size)
        super(self.__class__, type(self)).height.fset(self, new_size)
