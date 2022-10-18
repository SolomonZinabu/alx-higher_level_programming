#!/usr/bin/python3
<<<<<<< HEAD


def element_at(my_list, idx):
    """ Returns an element in a liust"""
    if idx < 0 or idx > len(my_list) - 1:
=======
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
        return None
    else:
        return my_list[idx]
