#!/usr/bin/pthon3
from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    if a < b:
        # Calculate initial sum
        c = add(a, b)
        # Add numbers from 4 to 5 to c
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        # Calculate difference
        return sub(a, b)
