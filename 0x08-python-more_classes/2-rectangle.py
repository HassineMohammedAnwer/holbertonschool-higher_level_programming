#!/usr/bin/python3
""" Classe Rectangle"""


class Rectangle:
    """ class Rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Return Rectangle Area

        Return: (int) rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """ returns the rectangle perimeter

        Return : (int) perimeter
        """
        if self.__height == 0 or self.__width ==0:
            return 0
        return(self.__height * 2) + (self.__width * 2)
