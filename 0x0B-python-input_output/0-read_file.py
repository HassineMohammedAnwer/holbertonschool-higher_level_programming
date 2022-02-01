#!/usr/bin/python3
"""READ a file"""


def read_file(filename=""):
    """ function name read_file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
