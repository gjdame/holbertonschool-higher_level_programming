#!/usr/bin/python3

"""Unittest for square([..])
"""

import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects == 0
        cls.s1 = Square(2, 2)
        cls.s2 = Square(size=4, x=2, y=3)

    def test_area(self):
        self.assertTrue(self.s1.area(), 4)
        self.assertTrue(self.s2.area(), 16)

    def test_fail(self):
        with self.assertRaises(TypeError):
            Square('A')
        with self.assertRaises(ValueError):
            Square(-4)
        with self.assertRaises(ValueError):
            Square(size=1, x=-1)
        with self.assertRaises(TypeError):
            Square(size=1, y='A')

    def test_str(self):
        self.assertEqual(str(self.s1), '[Square] (1) 2/0 - 2')
        self.assertEqual(str(self.s2), '[Square] (2) 2/3 - 4')

    def test_update(self):
        tmp = Square(5)
        tmp.update(10)
        self.assertEqual(str(tmp), '[Square] (10) 0/0 - 5')
        tmp.update(1, 2)
        self.assertEqual(str(tmp), '[Square] (1) 0/0 - 2')
        tmp.update(1, 2, 3)
        self.assertEqual(str(tmp), '[Square] (1) 3/0 - 2')

if __name__ == '__main__':
    unittest.main()
