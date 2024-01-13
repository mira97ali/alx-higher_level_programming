#!/usr/bin/python3
"""Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.validate_is_integer(width, "width")
        self.validate_is_positive(width, "width")
        self.__width = width
        self.validate_is_integer(height, "height")
        self.validate_is_positive(height, "height")
        self.__height = height
        self.validate_is_integer(x, "x")
        self.validate_zero_or_bigger(x, "x")
        self.__x = x
        self.validate_is_integer(y, "y")
        self.validate_zero_or_bigger(y, "y")
        self.__y = y

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.__width,
            self.__height
        )

    def validate_is_integer(self, input, input_name):
        """validate input is integer"""
        if not isinstance(input, int):
            raise TypeError(f"{input_name} must be an integer")

    def validate_is_positive(self, input, input_name):
        """validate input is bigger than zero"""
        if not input > 0:
            raise ValueError(f"{input_name} must be > 0")

    def validate_zero_or_bigger(self, input, input_name):
        """validate input is equal to or bigger than zero"""
        if input < 0:
            raise ValueError(f"{input_name} must be >= 0")

    @property
    def width(self):
        """Width Getter"""
        return self.__width

    @width.setter
    def width(self, new_width):
        """Width Setter"""
        self.validate_is_integer(new_width, "width")
        self.validate_is_positive(new_width, "width")
        self.__width = new_width

    @property
    def height(self):
        """Height Getter"""
        return self.__height

    @height.setter
    def height(self, new_height):
        """Height Setter"""
        self.validate_is_integer(new_height, "height")
        self.validate_is_positive(new_height, "height")
        self.__height = new_height

    @property
    def x(self):
        """X Getter"""
        return self.__x

    @x.setter
    def x(self, new_x):
        """X Setter"""
        self.validate_is_integer(new_x, "x")
        self.validate_zero_or_bigger(new_x, "x")
        self.__x = new_x

    @property
    def y(self):
        """Y Getter"""
        return self.__y

    @y.setter
    def y(self, new_y):
        """Y Setter"""
        self.validate_is_integer(new_y, "y")
        self.validate_zero_or_bigger(new_y, "y")
        self.__y = new_y

    def area(self):
        """Calculate the area"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        allowed_args = ["id", "width", "height", "x", "y"]
        # Assign values based on the order of allowed_args
        if args:
            for index, arg in enumerate(args):
                setattr(self, allowed_args[index], arg)
        # Assign values based on keyword arguments
        for key, value in kwargs.items():
            if key in allowed_args:
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
