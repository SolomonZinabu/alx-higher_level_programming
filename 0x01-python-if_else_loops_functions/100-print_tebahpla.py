#!/usr/bin/python3
<<<<<<< HEAD
for ascii_num in range(122, 96, -1):
	if ascii_num % 2 == 1:
		ascii_num = ascii_num - 32
	print("{:c}".format(ascii_num), end='')
=======
i = 122
while i >= 97:
    flag = 0
    if i % 2 != 0:
        i = i - 32
        flag = 1
    print("{:s}".format(chr(i)), end="")
    if flag == 1:
        i = i + 32
    i = i - 1
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
