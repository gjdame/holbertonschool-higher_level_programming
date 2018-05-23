#!/usr/bin/python3

import unittest
import json
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import pep8
import sys
import os
from io import StringIO


class TestBase(unittest.TestCase):

    def checking(self):
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(save_to_file.__doc__)
        self.assertIsNotNone(from_json_string.__doc__)
        self.assertIsNotNone(create.__doc__)
        self.assertIsNotNone(load_from_file.__doc__)

    def test_style_base(self):
        """
        Tests for pep8
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
        p = style.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_00_documentation(self):
        """
        Test to see if documentation is
        created and correct
        """
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(hasattr(Base, "load_from_file"))

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects == 0
        cls.r1 = Rectangle(3, 5, 1, id=9)
        cls.r3 = Rectangle(2, 4, id=11)
        cls.s1 = Square(5, id=99)
        cls.s2 = Square(7, 9, 1, id=78)

    def test_to_json_string_AND_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(list_input, list)
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)

    def test_create(self):
        r1_dictionary = self.r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(self.r1.__str__(), '[Rectangle] (9) 1/0 - 3/5')
        self.assertEqual(r2.__str__(), '[Rectangle] (9) 1/0 - 3/5')
        self.assertFalse(self.r1 is r2)
        self.assertFalse(self.r1 == r2)

    def test_save_to_file_AND_load_from_file(self):
        list_rectangles_input = [self.r1, self.r3]

        Rectangle.save_to_file(list_rectangles_input)
        self.assertTrue(os.path.isfile('Rectangle.json'))
        with open('Rectangle.json', 'r') as f:
            r_total = sum(1 for _ in f)
        self.assertGreater(r_total, 0)
        list_rectangles_output = Rectangle.load_from_file()

        for rect in list_rectangles_input:
            self.assertIsInstance(rect, Rectangle)

        for rect in list_rectangles_output:
            self.assertIsInstance(rect, Rectangle)

        list_squares_input = [self.s1, self.s2]

        Square.save_to_file(list_squares_input)
        self.assertTrue(os.path.isfile('Square.json'))

        with open('Square.json', 'r') as f:
            s_total = sum(1 for _ in f)
        self.assertGreater(s_total, 0)
        list_squares_output = Square.load_from_file()

        for square in list_squares_input:
            self.assertIsInstance(square, Square)

        for square in list_squares_output:
            self.assertIsInstance(square, Square)

        Base._Base__nb_objects -= 4

    def test_empty(self):
        """Test to check from empty"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", mode="r") as myFile:
            self.assertEqual([], json.load(myFile))

    def test_None(self):
        """
        Test to check from none empty
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", mode="r") as myFile:
            self.assertEqual([], json.load(myFile))

if __name__ == "__main__":
    unittest.main()
