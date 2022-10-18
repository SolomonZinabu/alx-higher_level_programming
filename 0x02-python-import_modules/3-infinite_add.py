#!/usr/bin/python3
<<<<<<< HEAD
from sys import argv

if __name__ == "__main__":
    arg_num = len(argv) - 1
    if arg_num == 0:
        print("{}".format(arg_num))
    else:
        result = []
        for i in range(1, arg_num + 1):
            result.append(int(argv[i]))
        print("{}".format(sum(result)))
=======
if __name__ == "__main__":
    from sys import argv
    add = 0
    for s in argv[1:]:
        add += int(s)
    print("{:d}".format(add))
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
