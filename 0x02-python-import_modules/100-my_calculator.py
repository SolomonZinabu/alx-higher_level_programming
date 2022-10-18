#!/usr/bin/python3
<<<<<<< HEAD
import sys
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    argv = sys.argv[1:]
    arg_num = len(argv)
    if arg_num != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    elif sys.argv[2] not in '+-*/':
        print('Unknown operator. Available operators: +, -, *, and /')
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] is '+':
            print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
        elif sys.argv[2] is '-':
            print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
        elif sys.argv[2] is '*':
            print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
        elif sys.argv[2] is "/":
            print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
=======
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    a = int(argv[1])
    b = int(argv[3])
    ops = ["+", "-", "*", "/"]
    from calculator_1 import add, sub, mul, div
    funcs = [add, sub, mul, div]
    for i, s in enumerate(ops):
        if argv[2] == s:
            print("{} {} {} = {}".format(a, s, b, funcs[i](a, b)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
