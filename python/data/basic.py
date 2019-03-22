#!env python3
# -*- coding: utf-8 -*-

# type
num = 15
print(type(num))

t = (1,2,3)
print(type(t))

# isinstance
print(isinstance("hello", str))

from calendar import TextCalendar, Calendar 
tcal = TextCalendar()
print(isinstance(tcal, TextCalendar))
print(isinstance(tcal, Calendar))

# id
print(id(tcal))
