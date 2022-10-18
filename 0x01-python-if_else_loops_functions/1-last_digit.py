#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
<<<<<<< HEAD

if number < 0:
    last_digit = ((number * -1) % 10) * -1
else:
    last_digit = number % 10
if last_digit > 5:
    print("Last digit of {0:d} is {1:d} and is greater than 5"
        .format(number, last_digit))
elif last_digit == 0:
    print("Last digit of {0:d} is {1:d} and is 0"
        .format(number, last_digit))
elif last_digit < 6 and not 0:
    print("Last digit of {0:d} is {1:d} and is less than 6 and not 0"
        .format(number, last_digit))
=======
lastDigit = number % 10 if number > 0 else int(repr(number)[-1]) * -1

print("Last digit of {} is {} ".format(number, lastDigit), end="")

if lastDigit > 5:
    print("and is greater than 5")
elif lastDigit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
