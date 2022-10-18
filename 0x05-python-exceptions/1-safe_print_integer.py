#!/usr/bin/python3
<<<<<<< HEAD


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except:
        return False
    return True
=======
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
