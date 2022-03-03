#!/usr/bin/python3
""" rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
