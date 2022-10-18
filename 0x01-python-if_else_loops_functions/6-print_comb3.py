#!/usr/bin/python3
<<<<<<< HEAD

for i in range(0, 10):
    for j in range(1, 10):
        if i >= j:
            continue
        if i == 8 and j == 9:
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}".format(i, j), end=", ")
=======
for i in range(10):
    for j in range(i + 1, 10):
        print(
            "{}{}".format(i, j),
            end=", " if int(str(i) + str(j)) < 89 else "\n"
            )
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
