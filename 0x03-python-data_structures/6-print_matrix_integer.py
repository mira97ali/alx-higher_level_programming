#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for vector in matrix:
        for idx, element in enumerate(vector):
            print(
                "{:d}".format(element),
                end=" " if idx < len(vector) - 1 else ""
            )
        print("{}".format("\n"), end="")
