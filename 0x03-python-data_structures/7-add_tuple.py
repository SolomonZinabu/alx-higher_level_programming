#!/usr/bin/python3
<<<<<<< HEAD


def add_tuple(tuple_a=(), tuple_b=()):
    """Adds elements of 2 tuples"""
    if len(tuple_a) < 1:
        tuple_a = (0, 0)
    elif len(tuple_a) < 2:
        tuple_a = (tuple_a[0], 0)
    if len(tuple_b) < 1:
        tuple_b = (0, 0)
    elif len(tuple_b) < 2:
        tuple_b = (tuple_b[0], 0)
    res = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return res
=======
def add_tuple(tuple_a=(), tuple_b=()):
    # If too long, cut the tuple to the first 2 elements
    # if too short, extend the tuple to match length 2
    a = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    b = tuple_b[:2] + (0,) * (2 - len(tuple_b))
    c = [x + y for x, y in zip(a, b)]
    return tuple(c[0:2])
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
