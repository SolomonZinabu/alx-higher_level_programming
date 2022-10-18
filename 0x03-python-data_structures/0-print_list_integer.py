#!/usr/bin/python3
<<<<<<< HEAD


def print_list_integer(my_list=[]):
    """Prints integers in a list"""
    for i in my_list:
        print("{:d}".format(i))
=======
def print_list_integer(my_list=[]):
    for i in my_list:
        if type(i) is int:
            print("{}".format(i))
        elif type(i) is str:
            try:
                print("{:d}".format(i))
            except TypeError:
                print("The value {} cannot be converted \
                        into integer.".format(i))
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
