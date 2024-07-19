#!/usr/bin/python3

def pow(a, b):
    """Computes a to the power of b and prints the result."""
    if b == 0:
        print(1)
    elif b > 0:
        result = 1
        for _ in range(b):
            result *= a
        print(result)
    else:
        result = 1
        for _ in range(-b):
            result *= a
        print(1 / result)
