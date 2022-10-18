#!/usr/bin/python3
<<<<<<< HEAD


def square_matrix_simple(matrix=[]):
    return list(map(lambda submat: list(map(lambda e: e**2, submat)), matrix))
=======
def square_matrix_simple(matrix=[]):
    return [list(map((lambda x: x * x), elm)) for elm in matrix]
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
