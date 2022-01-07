#!/usr/bin/python3
def best_score(a_dictionary):
    t = 0
    s = ""
    if a_dictionary:
        for i, j in a_dictionary.items():
            if j > t:
                s = i
                t = j
        return s
    else:
        return None
