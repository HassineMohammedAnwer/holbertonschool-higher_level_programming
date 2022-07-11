#!/usr/bin/python3
"""Find a peak"""


def find_peak(l):
    """a function that finds a peak in a list of unsorted integers."""
    if l == []:
        return
    if l[0] >= l[1]:
        return l[0]
    if l[len(l) - 1] >= l[len(l) - 2]:
        return l[len(l) - 1]
    for i in range(1, (len(l) - 1)):
        if ((l[i] >= l[i - 1]) and (l[i] >= l[i + 1])):
            return l[i]
