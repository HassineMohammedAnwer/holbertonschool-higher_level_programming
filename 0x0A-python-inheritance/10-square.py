#!/usr/bin/python3
""" class Square inherited from Rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ new class Square """

    def __init__(self, size):
        self.__size = size
        super().integer_validator('size', size)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))

    def area(self):
        return self.__size ** 2
