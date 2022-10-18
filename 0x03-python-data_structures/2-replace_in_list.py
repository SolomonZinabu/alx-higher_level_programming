#!/usr/bin/python3
<<<<<<< HEAD


def replace_in_list(my_list, idx, element):
    """Replaces element of a list at specified index"""
    if idx < 0 or idx > len(my_list) - 1:
=======
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
        return my_list
    else:
        my_list[idx] = element
        return my_list
