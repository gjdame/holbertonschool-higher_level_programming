 #!/usr/bin/python3


import unittest
from models.rectangle import Rectangle
from models.base import Base
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):

    def checking(self):
        self.assertIsNotNone(Base.__doc__)

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects == 0
        cls.r1 = Rectangle(10, 2)
        cls.r3 = Rectangle(2, 4, 2, 2, 12)

    def test_ids(self):
        self.assertEqual(self.r1.id, 2)
        self.assertEqual(self.r3.id, 12)
        self.r3.id = "a"
        self.assertEqual(self.r3.id, "a")

    def test_attr_errors(self):
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r11 = Rectangle(10, "2")
        with self.assertRaises(ValueError, msg="height must be  > 0"):
            r11 = Rectangle(-2, 1)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r11 = Rectangle({1: 2}, 2)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r21 = Rectangle(10, 2)
            r21.width = -10
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r31 = Rectangle(10, 2)
            r31.x = {}
        with self.assertRaises(ValueError, msg="y must be >=0"):
            r41 = Rectangle(10, 2, 3, -1)

    def test_areas(self):
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r3.area(), 8)

    def test_display(self):
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        self.r1.display()
        sys.stdout = old_stdout
        self.assertEqual(mystdout.getvalue(), "##########\n##########\n")
        sys.stdout = mystdout = StringIO()
        self.r3.display()
        self.assertEqual(mystdout.getvalue(), "\n\n  ##\n  ##\n  ##\n  ##\n")
        sys.stdout = old_stdout

    def test_str(self):
        self.assertEqual(self.r1.__str__(), "[Rectangle] (2) 0/0 - 10/2")
        self.assertEqual(self.r3.__str__(), "[Rectangle] (a) 2/2 - 2/4")

    def test_update(self):
        self.r1.update(89)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 0/0 - 10/2")
        self.r1.update(89, 2)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 0/0 - 2/2")
        self.r1.update(89, 2, 3)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 0/0 - 2/3")
        self.r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        with self.assertRaises(ValueError, msg="x must be >=0"):
            self.r1.update(y=1, width=2, x=-3, id=89)

    def test_dictionary(self):
        r1_dictionary = self.r1.to_dictionary()
        self.assertDictEqual(r1_dictionary, {
            'x': 0, 'y': 0, 'width': 10, 'height': 2, 'id': 2})
        r3_dictionary = self.r3.to_dictionary()
        self.assertDictEqual(r3_dictionary, {
            'x': 2, 'y': 2, 'width': 2, 'height': 4, 'id': 12})

    def test_to_json(self):
        dict = self.r1.to_dictionary()
        self.assertIsInstance(Base.to_json_string(dict), str)

if __name__ == '__main__':
    unittest.main()
