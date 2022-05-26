#!/usr/bin/python3
"""Module for add_integer method
    Returns:
    integer: the addition of a and b
    Raises:  TypeError: if a or b are not integers or floats
    Adds 2 integers"""

def add_integer(a, b=98):
    """Args:
            int a: first arg num
            int b: second arg num, default value = 98"""
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    if type(a) != int:
        raise TypeError('a must be an integer')
    if type(b) != int:
        raise TypeError('b must be an integer')
    else:
        return a + b
