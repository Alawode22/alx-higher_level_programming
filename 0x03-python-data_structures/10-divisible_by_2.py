#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    for item in my_list:
        if item % 2 == 0:
            return True
        else:
            return False
