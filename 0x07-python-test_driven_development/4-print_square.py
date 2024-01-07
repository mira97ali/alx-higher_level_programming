#!/usr/bin/python3
"""Print square"""


def print_square(size):
    """Print a square of '#' characters.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size < 0 or if size is a float and < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0 or (isinstance(size, float) and size < 0):
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
