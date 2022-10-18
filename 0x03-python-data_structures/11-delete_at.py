#!/usr/bin/python3
<<<<<<< HEAD


def delete_at(my_list=[], idx=0):
    """Deletes item ata specific index in a list"""
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        del my_list[idx]
        return my_list
=======
def delete_at(my_list=[], idx=0):

    if my_list is not None and 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
