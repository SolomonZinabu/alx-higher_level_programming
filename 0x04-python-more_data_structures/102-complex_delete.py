#!/usr/bin/python3
<<<<<<< HEAD


def complex_delete(a_dictionary, value):
    for x in list(a_dictionary.keys()):
        if a_dictionary[x] is value:
            del a_dictionary[x]
    return a_dictionary
=======
def complex_delete(my_dict, value):
    tmp = my_dict.copy()
    for k, v in tmp.items():
        if value == v:
            my_dict.pop(k)
    return my_dict
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
