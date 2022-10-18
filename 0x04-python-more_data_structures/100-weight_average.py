#!/usr/bin/python3
<<<<<<< HEAD


def weight_average(my_list=[]):
    return sum([x[0] * x[1] for x in my_list]) / \
        (sum([x[1] for x in my_list]) or 1)
=======
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    return sum([x*y for (x, y) in my_list]) / sum([y for (x, y) in my_list])
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
