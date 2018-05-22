#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import sys
from io import StringIO


class TestBase(unittest.TestCase):

    def checking(self):
        self.assertIsNotNone(Base.__doc__)

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects == 0
        cls.r1 = Rectangle(3, 5, 1, id=9)
        cls.r3 = Rectangle(2, 4, id=11)
        cls.s1 = Square(5, id=99)
        cls.s2 = Square(7, 9, 1, id=78)

    def test_to_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(list_input, list)
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)

    def test_dict_to_dict_instance(self):
        r1_dictionary = self.r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(self.r1.__str__(), '[Rectangle] (9) 1/0 - 3/5')
        self.assertEqual(r2.__str__(), '[Rectangle] (9) 1/0 - 3/5')
        self.assertFalse(self.r1 is r2)
        self.assertFalse(self.r1 == r2)

    def test_instances(self):
        list_rectangles_input = [self.r1, self.r3]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        for rect in list_rectangles_input:
            self.assertIsInstance(rect, Rectangle)

        for rect in list_rectangles_output:
            self.assertIsInstance(rect, Rectangle)

        list_squares_input = [self.s1, self.s2]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        for square in list_squares_input:
            self.assertIsInstance(square, Square)

        for square in list_squares_output:
            self.assertIsInstance(square, Square)

        Base._Base__nb_objects -= 4

if __name__ == "__main__":
    unittest.main()
