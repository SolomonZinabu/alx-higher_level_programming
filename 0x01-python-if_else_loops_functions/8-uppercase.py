#!/usr/bin/python3
<<<<<<< HEAD


def uppercase(str):
    result = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
        print("{:s}".format(result))
=======
def uppercase(str):
    tmp = list(str)
    for i in range(len(tmp)):
        if (ord(tmp[i]) > 96 and ord(tmp[i]) < 123):
            tmp[i] = chr(ord(tmp[i]) - 32)
    print("{}".format("".join(tmp)))
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
