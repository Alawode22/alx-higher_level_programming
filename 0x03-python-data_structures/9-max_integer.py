#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    highest = my_list[0]
    for num in my_list[1:]:
        if num > highest:
            highest = num
    return highest
