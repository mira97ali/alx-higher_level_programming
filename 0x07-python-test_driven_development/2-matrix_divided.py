#!/usr/bin/python3
"""divides all elements of a matrix"""


common_error = "matrix must be a matrix (list of lists) of integers/floats"


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a divisor.

        Args:
            matrix (list): A matrix (list of lists)
                           containing only integers or floats.
            div (int or float): The divisor to divide all matrix elements.

        Raises:
            TypeError: If the matrix is not a valid matrix,
                       or if any element is not an integer or float,
                       or if each row of the matrix doesn't have the same size,
                       or if div is not a number.
            ZeroDivisionError: If div is equal to 0.

        Returns:
            - list: A new matrix with each element rounded
                    to 2 decimal places after division.
    """
    if not matrix or not isinstance(matrix, list):
        raise TypeError(common_error)

    for vector in matrix:
        if not isinstance(vector, list):
            raise TypeError(common_error)

        for value in vector:
            if not isinstance(value, (float, int)):
                raise TypeError(common_error)

    if not all(len(row) == len(matrix[0]) for row in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(value / div, 2) for value in row] for row in matrix]
