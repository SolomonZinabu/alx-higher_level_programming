#!/usr/bin/python3
<<<<<<< HEAD

if __name == "__main__":
    import sys
    argv = sys.argv[1:]
    arg_num = len(argv)
    i = 1
    if arg_num == 0:
        print("{:d} arguments.".format(arg_num))
    elif arg_num == 1:
        print("{:d} argument.".format(arg_num))
        print("{:d}: {:s}".format(i, sys.argv[1]))
    else:
        print("{:d} arguments.".format(arg_num))
        while i < arg_num:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1
=======
if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    print("{:d} {:s}{:s}".format(l - 1, "argument" if l <= 2 else "arguments",
                                 "." if l == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
