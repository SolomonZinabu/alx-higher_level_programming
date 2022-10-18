#!/usr/bin/python3
<<<<<<< HEAD


def square_matrix_map(matrix=[]):
    return list(map(lambda submat: list(map(lambda e: e**2, submat)), matrix))
=======
def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda col: col**2, row)), matrix))
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
