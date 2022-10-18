#!/usr/bin/python3
<<<<<<< HEAD

for i in range(100):
    if i < 99:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:d}".format(i))
=======
for i in range(100):
    print("{:0>2}".format(i), end=", " if i < 99 else "\n")
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
