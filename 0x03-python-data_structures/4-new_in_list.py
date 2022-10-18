#!/usr/bin/python3
<<<<<<< HEAD


def new_in_list(my_list, idx, element):
    """Makes copy of a list, replce element at certain index in copy
       while leaving originial unmodified.
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list[:]
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
    
=======
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        mod_list = my_list[:]
        mod_list[idx] = element
        return mod_list
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
