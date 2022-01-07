#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    n = sum([x * y for x, y in my_list])
    res = n / sum([y for x, y in my_list])
    return res
