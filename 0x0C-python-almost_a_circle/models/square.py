#!/usr/bin/python3
"""
...
"""


from curses.textpad import rectangle
from models.rectangle import Rectangle

class Square(Rectangle)
"""
...
"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id)
        
        self.__size = size
        self.x = x
        self.y = y
