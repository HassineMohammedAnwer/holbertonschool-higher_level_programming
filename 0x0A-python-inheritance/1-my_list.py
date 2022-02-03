#!/usr/bin/python3
""" class MyList """


class MyList(list):
    """  prints sorted list """

    def print_sorted(self):
        print(sorted(self))
