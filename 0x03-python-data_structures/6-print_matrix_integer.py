#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for cel in matrix:
        for i in range(len(cel)):
            if i < len(cel) - 1:
                print("{:d}".format(cel[i]), end=" ")
            else:
                print("{:d}".format(cel[i]))
