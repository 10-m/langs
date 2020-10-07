#!env python3
# -*- coding: utf-8 -*-
from dataclasses import dataclass

@dataclass(order=True)
class Person:
    name: str
    age: int = 20

p1 = Person('Alice')
p2 = Person('Bob', 18)
print(p1, p2)
print(p1 < p2)
