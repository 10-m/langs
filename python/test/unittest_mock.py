#!env python3
# -*- coding: utf-8 -*-
import unittest
from unittest import mock
from unittest_mock_target import add_time, get_this_month
from datetime import datetime

def get_username(user):
    return user.username

class TestMock(unittest.TestCase):
    def test_mock(self):
        dummy_object = mock.Mock()
        dummy_object.username = 'joe'
        self.assertEqual(get_username(dummy_object), 'joe')

    @mock.patch('unittest_mock_target.time')
    def test_mock_patch(self, m):
        m.return_value = 1470620400
        self.assertEqual(add_time(), 1470624000)

    @mock.patch('unittest_mock_target.get_now')
    def test_builtin_func(self, m):
        m.return_value = datetime(2015, 8, 1, 12, 32, 0)
        self.assertEqual(get_this_month(), 8)

if __name__ == '__main__':
    unittest.main()
