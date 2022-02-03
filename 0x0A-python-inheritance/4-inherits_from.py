#!/usr/bin/python3
""" method inherits_from """


def inherits_from(obj, a_class):
    """check if is instance of an inherited class"""

    return isinstance(obj, a_class) and type(obj) != a_class
