#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    multiples = {}
    for key in a_dictionary:
        multiples[key] = (lambda x: x * 2)(a_dictionary[key])
    return multiples
