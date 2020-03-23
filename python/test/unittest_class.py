#!env python3
# -*- coding: utf-8 -*-
import unittest

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fullname(self):
        return self.first_name + ' ' + self.last_name

class TestUser(unittest.TestCase):
    def test_fullname(self):
        user = User('Hiroki', 'Kiyohara')
        self.assertEqual(user.fullname(), 'Hiroki Kiyohara')

if __name__ == '__main__':
    unittest.main()
