#!/usr/bin/python3
<<<<<<< HEAD


def safe_print_division(a, b):
    try:
        a = a / b
    except ZeroDivisionError:
        a = None
    finally:
        print("Inside result:", "{}".format(a))
    return a
=======
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
