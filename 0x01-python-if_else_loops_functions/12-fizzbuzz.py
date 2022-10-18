#!/usr/bin/python3
<<<<<<< HEAD


def fizzbuzz()
	for i in range(1, 101):
		if i % 3 == 0 and i % 5 == 0:
			print("FizzBuzz", end=" ")
		elif i % 5 == 0:
			print("Buzz", end=" ")
		elif i % 3 == 0:
			print("Fizz", end=" ")
		else:
			print("{:d}".format(i), end=" ")
=======
def fizzbuzz():
    for i in range(1, 101):
        if (i % 15 == 0):
            print("FizzBuzz ", end="")
        elif (i % 3 == 0):
            print("Fizz ", end="")
        elif (i % 5 == 0):
            print("Buzz ", end="")
        else:
            print("{:d} ".format(i), end="")
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
