#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        if i != j:
            if i == 9 and j == 8:
                print("{:02}".format(i * 10 + j))
            else:
                print("{:02d}, ".format(i * 10 + j), end="")
