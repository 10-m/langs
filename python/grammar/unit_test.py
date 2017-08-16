#!env python3
# -*- coding: utf-8 -*-

import unittest

class Turu:
    def get_name(self):
        return "turu"
    def get_legs(self):
        return 2

class Kame:
    def get_name(self):
        return "kame"
    def get_legs(self):
        return 4

def calc_turukame(turu, kame, heads, legs):
    turu_leg = turu.get_legs()
    kame_leg = kame.get_legs()
    kame_num = (legs - (turu_leg * heads)) // (kame_leg - turu_leg)
    turu_num = heads - kame_num
    print("head=", heads, "leg=", legs)
    print(turu.get_name(), "=", turu_num)
    print(kame.get_name(), "=", kame_num)
    return (turu_num, kame_num)

calc_turukame(Turu(), Kame(), heads=10, legs=28)

class TestTurukame(unittest.TestCase):
    def test_turukame(self):
        turu, kame = calc_turukame(Turu(), Kame(), heads=10, legs=28)
        self.assertEqual(turu, 6, "num_of_turu")
        self.assertEqual(kame, 4, "num_of_turu")
