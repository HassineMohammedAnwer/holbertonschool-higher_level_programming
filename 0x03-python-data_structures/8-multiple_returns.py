#!/usr/bin/python3
def multiple_returns(sentence):
    n_tuple = ()
    if len(sentence) == 0:
        n_tuple = 0, "None"
    else:
        n_tuple = len(sentence), sentence[0]
    return n_tuple
