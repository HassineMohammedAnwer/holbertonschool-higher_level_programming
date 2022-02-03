#!/usr/bin/python3
""" class Rectangle inherited from BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ new class rectangle """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator('width', width)
        super().integer_validator('height', height)
