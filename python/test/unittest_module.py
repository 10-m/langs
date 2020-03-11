#!env python3
# -*- coding: utf-8 -*-
import unittest

class Calc:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def is_even(self, num):
        return num // 2

class CalcTest1(unittest.TestCase):
    def test_add(self):
        c = Calc()
        expected = 5
        actual = c.add(2, 3)
        self.assertEqual(expected, actual)

    def test_sub(self):
        c = Calc()
        expected = 3
        actual = c.sub(5, 2)
        self.assertEqual(expected, actual)

    def test_is_even(self):
        self.assertTrue(Calc().is_even(2))

    def test_is_odd(self):
        self.assertFalse(Calc().is_even(1))

class CalcTest2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        
    def setUp(self):
        self.calc = Calc()
        print("setUp", id(self))

    def tearDown(self):
        print("tearDown", id(self))
         
    def test_add(self):
        expected = 5
        actual = self.calc.add(2, 3)
        self.assertEqual(expected, actual)

    def test_sub(self):
        expected = 3
        actual = self.calc.sub(5, 2)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
