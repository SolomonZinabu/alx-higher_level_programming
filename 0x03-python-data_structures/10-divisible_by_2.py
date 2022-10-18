#!/usr/bin/python3
<<<<<<< HEAD


def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list"""
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
=======
def divisible_by_2(my_list=[]):
    if not my_list:
        return
    new_list = [n % 2 == 0 for n in my_list]

>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
    return new_list
