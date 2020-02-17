#!env python3
# -*- coding: utf-8 -*-

# postion
print('{}, {}!'.format('Hello', 'World'))
print('{1}, {0}!'.format('Hello', 'World'))
print('{0}, {1}, {0}!'.format('Hello', 'World'))

# name
print('{name} {age}'.format(name='aaa', age=123))

# number
x = 11
y = 2.5555555
z = 1000000
print('{:d}'.format(x))
print('{:5d}'.format(x)) # 右詰め
print('{:05d}'.format(x)) # ゼロ詰め
print('{:f}'.format(y))
print('{:.2f}'.format(y)) 
print('{:,}'.format(z))# 1,000,000
