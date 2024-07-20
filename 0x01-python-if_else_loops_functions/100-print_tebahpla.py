#!/usr/bin/python3

for i in range(122, 96, -1):  # ASCII values from 'z' to 'a'
    if i % 2 == 0:  # Even indices for lowercase
        print("{}".format(chr(i)), end="")
    else:  # Odd indices for uppercase
        print("{}".format(chr(i - 32)), end="")

