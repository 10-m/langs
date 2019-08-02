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

# issubclass
import calendar
print(issubclass(calendar.TextCalendar, calendar.Calendar))

# globals, locals
def test(num):
    msg = 'hello' * num
    print('---locals')
    print(locals())

num = 3
test(num)
print('---globals')
print(globals())

# is (check the same object)
l1 = ['a', 'b', 'c']
l2 = ['a', 'b', 'c']
l3 = l1
print(l1 is l2)
print(l1 is l3)

# all
print(all([True, False, False]))

# any
print(any([True, False, False]))
