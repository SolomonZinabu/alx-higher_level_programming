#!/usr/bin/python3
<<<<<<< HEAD


def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]
    return a_dictionary
=======
def simple_delete(my_dict, key=""):
    my_dict.pop(key, None)
    return my_dict
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
