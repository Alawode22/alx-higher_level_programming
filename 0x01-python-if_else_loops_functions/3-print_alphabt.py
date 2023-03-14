#!/usr/bin/python3
for b in range(97, 123):
    if (b == 101 or b == 113):
        continue
    print("{}".format(chr(b)), end="")
