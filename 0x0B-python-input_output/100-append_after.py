#!/usr/bin/python3
"""insert a line of text in a file """


def append_after(filename="", search_string="", new_string=""):
    """append text after in file"""
    with open(filename, "r+", encoding="utf-8") as f:
        tmp = ""
        for line in f:
            tmp += line
            if search_string in line:
                tmp += new_string
        f.seek(0)
        f.write(tmp)
