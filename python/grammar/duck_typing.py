#!env python3
# -*- coding: utf-8 -*-

def test_duck(it):
    it.sound()
    it.walk()

class Duck:
    def sound(self):
        print("Ga-Ga-")

    def walk(self):
        print("a duck walking")

class Dog:
    def sound(self):
        print("Baw")

    def walk(self):
        print("a dog walking")

duck = Duck()
test_duck(duck)

dog = Dog()
test_duck(dog)
