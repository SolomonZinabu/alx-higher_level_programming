#!/usr/bin/python3
<<<<<<< HEAD


def print_last_digit(number):
    if number < 0:
        number = ((-1) * number) % 10
    else:
        number = number % 10

    print("{:d}".format(number), end="")
    return number
=======
def print_last_digit(number):
    tmp = int(repr(number)[-1])
    print("{}".format(tmp), end="")
    return tmp
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
