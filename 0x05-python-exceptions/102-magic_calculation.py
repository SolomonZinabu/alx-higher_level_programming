#!/usr/bin/python3
<<<<<<< HEAD


=======
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
<<<<<<< HEAD
                raise Exception("Too far")
=======
                raise Exception('Too far')
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
            else:
                result += (a ** b) / i
        except:
            result = b + a
            break
    return result
