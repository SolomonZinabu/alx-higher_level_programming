#!/usr/bin/python3
<<<<<<< HEAD
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
=======
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
<<<<<<< HEAD
        return sub(a, b)
    return 0
=======
        return (sub(a, b))
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
