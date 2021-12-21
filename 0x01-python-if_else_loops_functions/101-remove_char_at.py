#!/usr/bin/python3
def remove_char_at(str, n):
    x = ''
    i = 0
    for ch in str:
        if i != n:
            x += str[i]
        i += 1
    return x
