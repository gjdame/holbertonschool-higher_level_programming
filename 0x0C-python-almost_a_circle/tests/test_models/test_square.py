#!/usr/bin/python3

"""Unittest for square([..])
"""

import unittest
from io import StringIO
import sys
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):

    def checking(self):
        self.assertIsNotNone(Square.__doc__)
        self.assertIsNotNone(size.__doc__)
        self.assertIsNotNone(update.__doc__)
        self.assertIsNotNone(to_dictionary.__doc__)

    def test_style_square(self):
        """
        Tests for pep8
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
        p = style.check_files(['models/square.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects == 0
        cls.s1 = Square(2, 2)
        cls.s2 = Square(size=4, x=2, y=3)

    def test_id(self):
        self.assertTrue(self.s1.id, 1)
        self.assertTrue(self.s2.id, 2)

    def test_area(self):
        self.assertTrue(self.s1.area(), 4)
        self.assertTrue(self.s2.area(), 16)

    def test_attr_square(self):
        with self.assertRaises(TypeError):
            Square('A')
        with self.assertRaises(ValueError):
            Square(-4)
        with self.assertRaises(ValueError):
            Square(size=1, x=-1)
        with self.assertRaises(TypeError):
            Square(size=1, y='A')

    def test_str(self):
        self.assertEqual(str(self.s1), '[Square] (3) 2/0 - 2')
        self.assertEqual(str(self.s2), '[Square] (4) 2/3 - 4')

    def test_update(self):
        tmp = Square(5)
        tmp.update(10)
        self.assertEqual(str(tmp), '[Square] (10) 0/0 - 5')
        tmp.update(1, 2)
        self.assertEqual(str(tmp), '[Square] (1) 0/0 - 2')
        tmp.update(1, 2, 3)
        self.assertEqual(str(tmp), '[Square] (1) 3/0 - 2')

    def test_display(self):
        Base._Base__nb_objects = 0
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        r1 = Square(4)
        r1.display()
        sys.stdout = old_stdout
        self.assertEqual(mystdout.getvalue(), "####\n####\n####\n####\n")
        sys.stdout = mystdout = StringIO()
        r1 = Rectangle(2, 2, 2, 2)
        r1.display()
        self.assertEqual(mystdout.getvalue(), "\n\n  ##\n  ##\n")
        sys.stdout = old_stdout

    def test_dictionary(self):
        Base._Base__nb_objects = 0
        r1 = Square(2, 2, 2, 2)
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(r1_dictionary, {
            'x': 2, 'y': 2, 'size': 2, 'id': 2})
        r1 = Rectangle(1, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(r1_dictionary, {
            'x': 0, 'y': 0, 'width': 1, 'height': 1, 'id': 1})

if __name__ == '__main__':
    unittest.main()
