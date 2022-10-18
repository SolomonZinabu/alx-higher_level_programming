#!/usr/bin/python3
<<<<<<< HEAD
if __name__ = "__main__":
    import sys
    import hidden_4
    for n in dir(hidden_4):
        if n[:2] != "__":
            print(n)
=======
import hidden_4


def discovr():
    name = dir(hidden_4)
    for i in name:
        if i[:2] != '__':
            print("{:s}".format(i))


if __name__ == "__main__":
    discovr()
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
