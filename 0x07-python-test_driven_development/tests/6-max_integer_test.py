#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def testForImport(self):
        self.assertTrue(__import__('6-max_integer').max_integer)

    def testBasic(self):
        my_list = [1, 3, 2, 4]
        self.assertEqual(max_integer(my_list), 4)

    def testBasic2(self):
        A = 52
        my_list = [1, 2, 4, A]
        self.assertEqual(max_integer(my_list), A)

    def testOneElement(self):
        my_list = [1]
        self.assertEqual(max_integer(my_list), 1)

    def testEmpty(self):
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def testWord(self):
        my_list = ['what', 'off', 'gumby']
        self.assertEqual(max_integer(my_list), 'what')

    def testFailBasic(self):
        my_list = [1, 4, 'A']
        self.assertRaises(TypeError, max_integer, my_list)

    def testFailDict(self):
        my_list = {'a': 2, 'b': 1, 'c': 3}
        self.assertRaises(KeyError, max_integer, my_list)

    def testPassDict(self):
        my_list = {0: 'a', 1: 'z', 2: 'c'}
        self.assertEqual(max_integer(my_list), 'z')


if __name__ == '__main__':
    unittest.main()
