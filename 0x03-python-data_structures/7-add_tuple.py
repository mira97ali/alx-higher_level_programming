#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = fill_gaps(tuple_a)
    tuple_b = fill_gaps(tuple_b)
    result1 = tuple_a[0] + tuple_b[0]
    result2 = tuple_a[1] + tuple_b[1]
    return (result1, result2)


def fill_gaps(tuple_x):
    if not tuple_x:
        tuple_x = (0, 0)
    if len(tuple_x) == 1:
        tuple_x = (tuple_x[0], 0)
    return tuple_x
