#!/usr/bin/python3
<<<<<<< HEAD


def print_reversed_list_integer(my_list=[]):
    """Print integers of a list in reversed order"""
    if my_list:
        for i in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[i]))
=======
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    for i in reversed(my_list):
        print("{:d}".format(i))
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
