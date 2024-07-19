#!/usr/bin/python3
def uppercase(str):
    new_str = []
    for char in str:
        if 'a' <= char <= 'z':
            upp_char = chr(ord(char) - 32)
        else:
            upp_char = char
        new_str.append(upp_char)
    upp_str = ''.join(new_str)
    print("{}".format(upp_str))
