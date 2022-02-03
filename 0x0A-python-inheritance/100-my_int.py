#!/usr/bin/python3
"""a class inherited from int"""


class MyInt(int):
    """ a class MyInt"""

    def __eq__(self, x):
        return not super().__eq__(x)

    def __ne__(self, x):
        return not super().__ne__(x)
