#!/usr/bin/python3
"""
...
"""


from curses.textpad import rectangle
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    ...
    """

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        ...
        """
        return str(f"[Square] ({self.id}) <self.x>/<self.y> - <self.size>)")
