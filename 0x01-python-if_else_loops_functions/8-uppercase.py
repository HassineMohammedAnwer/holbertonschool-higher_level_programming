#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            c = chr(ord(i) - 32)
        else:
            c = i
        print("{:s}".format(c), end="")
    print('')
