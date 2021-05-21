#!/usr/bin/python3
"""
tests for max_integer modul with unittest
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase)

    def test_int_in_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_float_in_list(self):
        self.assertEqual(max_integer([3.0, 2.0, 5.0]), 5.0)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_no_input(self):
        self.assertIsNone(max_integer(), None)

    def test_neg_int_in_list(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_string(self):
        self.assertEqual(max_integer("Hello"), 'o')

if __name__ == '__main__':
    unittest.main()
