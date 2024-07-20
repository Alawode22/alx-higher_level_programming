#!/usr/bin/python3

import sys

if __name__ == "__main__":
    a = 0
    for i in range(1, len(sys.argv)):
        a += nt(sys.argv[i])
    print(a)
