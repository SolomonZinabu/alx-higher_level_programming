#!/usr/bin/python3
<<<<<<< HEAD


def max_integer(my_list=[]):
    """Returns largest int of a list"""
    if my_list:
        my_list.sort()
        return my_list[-1]
    else:
        return None
=======
def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for elm in my_list:
            if elm > max:
                max = elm
        return max
    return None
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
