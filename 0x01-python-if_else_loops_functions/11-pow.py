#!/usr/bin/python3
<<<<<<< HEAD


def pow(a, b):
	# i want to create a variable that holds result of product.
	res = 1
	base = 1
	numb = 0

	if b < 0:
		numb = b
		b = (-1) * b

	for i in range(b):
		res *= a
		base = res * res

	if numb  < 0:
		res /= base
	return result
=======
def pow(a, b):
    return a ** b
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
