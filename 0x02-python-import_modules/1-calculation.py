#!/usr/bin/python3
<<<<<<< HEAD

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

=======
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
