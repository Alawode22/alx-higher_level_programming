#!/usr/bin/python3
def islower(c):
    # Check if c is a single lowercase character
    return isinstance(c, str) and len(c) == 1 and 'a' <= c <= 'z'
