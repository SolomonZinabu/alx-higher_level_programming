#!/usr/bin/python3
<<<<<<< HEAD


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxval = 0
    maxkey = None
    for k, v in a_dictionary.items():
        if v > maxval:
            maxval = v
            maxval = k
    return maxkey
=======
def best_score(my_dict):
    return max(my_dict, key=my_dict.get) if my_dict else None
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
