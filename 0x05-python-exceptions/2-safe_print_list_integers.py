#!/usr/bin/python3
<<<<<<< HEAD


def safe_print_list_integers(my_list=[], x=0):
    i, j = 0, 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            j += 1
        except (ValueError, TypeError):
            pass
        i += 1
    print()
    return j
=======
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            c += 1
        except (ValueError, TypeError):
            continue
    print()
    return c
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
