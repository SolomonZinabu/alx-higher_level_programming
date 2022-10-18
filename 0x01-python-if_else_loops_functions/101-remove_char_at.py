#!/usr/bin/python3
<<<<<<< HEAD


def remove_char_at(str, n):
	if n < 0:
		return str
	return (str[0:n] + str[n + 1:])
=======
def remove_char_at(str, n):
    if n >= 0:
        str = str[:n] + str[n + 1:]
    return str
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
