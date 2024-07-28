#!/usr/bin/python3

def best_score(a_dictionary):
    biggest = next(iter(a_dictionary))
    for key in a_dictionary:
        if a_dictionary[key] > a_dictionary[biggest]:
            biggest = key
    return biggest
