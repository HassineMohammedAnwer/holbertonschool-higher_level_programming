#!/usr/bin/python3
""" class BaseGeometry """


class BaseGeometry():
    """  contains instance method area """

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        else:
            self.value = value
