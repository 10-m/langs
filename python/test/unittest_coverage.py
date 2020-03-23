#!env python3
# -*- coding: utf-8 -*-
import unittest

class TestCoverage(unittest.TestCase):
    def test_coverage(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
    # coverage run unittest_coverage.py
    # coverage report -m
