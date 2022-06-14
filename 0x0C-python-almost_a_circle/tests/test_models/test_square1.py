#!/usr/bin/python3
"""Unittest for class Square
"""
import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    """Testing Square
    """

    def set_id(self):
        """
        ...
        """
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_instance(self):
        """
        ...
        """
        s2 = Square(5)
        s6 = Square(3, 5)
        with self.assertRaises(TypeError):
            s1 = Square()
            s4 = Square("z")
            s5 = Square(4.6)
            s7 = Square(3, "a", "b")
            s12 = Square(None)
            s13 = Square(True)
            s14 = Square(8, False)
        with self.assertRaises(ValueError):
            s3 = Square(-3)
            s8 = Square(0)
            s9 = Square(2, -10)
            s10 = Square(2, 5, -7)
            s11 = Square(float('inf'))
        self.assertEqual(s2.id, 1)
        
