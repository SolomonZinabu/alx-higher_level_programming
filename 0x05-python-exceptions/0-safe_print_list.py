#!/usr/bin/python3
<<<<<<< HEAD


def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i is not x:
            print(my_list[i], end='')
            i += 1
    except IndexError:
        None
    print()
    return i
=======
def safe_print_list(my_list=[], x=0):
    c = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            c += 1
        except IndexError:
            break
    print()
    return c
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
