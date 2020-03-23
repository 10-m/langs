#!env python3
# -*- coding: utf-8 -*-
import unittest

class TestAssert(unittest.TestCase):
    def test_eqaul(self):
        actual = 1
        self.assertEqual(actual, 1)

    def test_is_none(self):
        actual = None
        self.assertIsNone(actual)

    def test_greater_equal(self):
        actual = 100
        self.assertGreaterEqual(actual, 10)

    def test_less(self):
        actual = 10
        self.assertLess(actual, 100)

    def test_in(self):
        actual = 'A'
        self.assertIn(actual, ['A', 'B', 'C'])

    def test_raise(self):
        with self.assertRaises(ValueError):
            raise ValueError

if __name__ == '__main__':
    unittest.main()
