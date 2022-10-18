#!/usr/bin/python3
<<<<<<< HEAD


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of ints"""
    for row in matrix:
        for i in row:
            if i != row[-1]:
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end="")
        print()
=======
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for col in range(len(line)):
            print(
                "{:d}".format(line[col]),
                end="" if col == len(line) - 1 else " ")
        print("")
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
