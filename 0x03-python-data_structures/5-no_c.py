#!/usr/bin/python3
<<<<<<< HEAD


def no_c(my_string):
    output = my_string.translate({ord(i): None for i in 'cC'})
    return output
=======
def no_c(my_string):
    string = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            string = string + c
    return string
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
