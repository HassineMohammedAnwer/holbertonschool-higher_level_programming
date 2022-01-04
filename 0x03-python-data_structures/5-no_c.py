#!/usr/bin/python3
def no_c(my_string):
    n_string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            n_string = n_string + i
    return n_string
