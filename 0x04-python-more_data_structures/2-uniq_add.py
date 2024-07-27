#!/usr/bin/python3

def uniq_add(my_list=[]):
    seen = set()
    added = 0
    for i in my_list:
        if i not in seen:
            seen.add(i)
            added += i
    return added
