#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy = {}
    for i in a_dictionary:
        copy[i] = a_dictionary[i] * 2
    return copy
