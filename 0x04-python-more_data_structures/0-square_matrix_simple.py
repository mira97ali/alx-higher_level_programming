#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for vector in matrix:
        new_vector = []
        for number in vector:
            power = number ** 2
            new_vector.append(power)
        new_matrix.append(new_vector)
    return new_matrix
