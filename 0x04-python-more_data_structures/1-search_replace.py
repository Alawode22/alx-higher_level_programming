#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = [replace if s == search else s for s in my_list]
    return new_list
