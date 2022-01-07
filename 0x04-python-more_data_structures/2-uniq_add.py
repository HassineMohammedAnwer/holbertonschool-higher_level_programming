#!/usr/bin/python3
def uniq_add(my_list=[]):
    cop = list(set(my_list))
    s = 0
    for i in cop:
        s += i
    return s
