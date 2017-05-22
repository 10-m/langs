#!env python3
# -*- coding: utf-8 -*-

import math

class CalcFee:
    def __init__(self):
        self.shipping_fee = 1000
        self.tax_rate = 0.08
        self.value = 0

    def addItem(self, price):
        self.value += price

    def calc(self):
        total = self.value + self.shipping_fee
        tax = math.ceil(total * self.tax_rate)
        v = math.ceil(total + tax)
        return v

    def print(self):
        print(self.calc(), "yen")

feel = CalcFee()
feel.addItem(500)
feel.print()

class Cat:
    # class variable
    nakigoe = "nya-"

    def naku(self):
        print(Cat.nakigoe)

    def naku2(self):
        print(self.nakigoe)

mike = Cat()
mike.naku()

nora = Cat()
nora.naku()

Cat.nakigoe = "myu-"
mike.naku()
nora.naku()

mike.naku2()
nora.naku2()
mike.nakigoe = "mew"
mike.naku2()
nora.naku2()
