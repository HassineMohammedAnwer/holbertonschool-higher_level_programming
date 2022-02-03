#!/usr/bin/python3
"""class Square."""


class Square:
    """name of class Square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):

        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for y in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()

    def __str__(self):
        new_str = ""
        if self.__size == 0:
            new_str = ''
            return new_str

        for i in range(0, self.__position[1]):
            new_str += '\n'
        for i in range(self.__size):
            for j in range (0, self.__position[0]):
                new_str += ' '
            for j in range(0, self.__size):
                new_str += '#'
            if i is not self.__size - 1:
                new_str += '\n'
        return new_str
