#!/usr/bin/python3
import random
number = random.randint(-10, 10)
<<<<<<< HEAD
if number > 0:
    print("{:d} is positive".format(number))
elif number == 0:
    print("{:d} is zero".format(number))
else:
    print("{:d} is negative".format(number))
=======
if number < 0:
    print("{:d} is negative".format(number))
elif number > 0:
    print("{:d} is positive".format(number))
else:
    print("0 is zero")
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
