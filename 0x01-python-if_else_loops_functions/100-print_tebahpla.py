#!/usr/bin/python3
for x in range(ord('z'), ord('a') - 1, -2):
    print("{:c}{:s}".format(x, chr(x - 33)), end="")
