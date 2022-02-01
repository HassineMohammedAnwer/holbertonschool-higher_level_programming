#!/usr/bin/python3
"""write a file"""


def append_write(filename="", text=""):
    """ function name write_file"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
