#!/usr/bin/python3
"""
find the peek
"""


def find_peak(l):
    """
        first or last element is peak element
    """
    if l == []:
        return
    if l[0] >= l[1]:
        return l[0]
    if l[len(l) - 1] >= l[len(l) - 2]:
        return l[len(l) - 1]
    """check for every other element"""
    for i in range(1, len(l) - 1):
        """check if the neighbors are smaller"""
        if l[i] >= l[i - 1] and l[i] >= l[i + 1]:
            return l[i]
