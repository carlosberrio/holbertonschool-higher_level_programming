#!/usr/bin/python3
"""Defines a class Rectangle
Method to calculate an area and perimeter
of a rectangle"""


class Rectangle:
    """Defines a Rectangle"""
    def __init__(self, width=0, height=0):
        """method that defines a rectangle sides"""
        self.width = width
        self.height = height
    @property
    def width(self):
        """method that defines the rectangle width"""
        return self.__width
    @width.setter
    def width(self, value):
        """method that defines the rectangle width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """method that defines the rectangle heiht"""
        return self.__height
    @height.setter
    def height(self, value):
        """method that defines the rectangle heiht"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        """method that returns the rectangle area"""
        return self.__width * self.__height
    def perimeter(self):
        """method that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
