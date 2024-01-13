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

    def update(self, *args, **kwargs):
        """assigns attributes based on arguments and keyword arguments"""
        allowed_args = ["id", "size", "x", "y"]
        # If *args is not empty, assign values based on the order of allowed_args
        if args:
            for index, arg in enumerate(args):
                setattr(self, allowed_args[index], arg)
        # Assign values based on keyword arguments
        for key, value in kwargs.items():
            if key in allowed_args:
                setattr(self, key, value)
