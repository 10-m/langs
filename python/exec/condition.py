#!env python3
# -*- coding: utf-8 -*-

## conditions
result1 = 'is' not in 'this'
print("'is' not in 'this':", result1)

result2 = 'OK' and None
print("'OK' and None:", result2)

result3 = 'OK' or None
print("'OK' or None:", result3)

## compare sequence
val = 'OK'
result4 = val is None
print("val is None:", result4)

result5 = 'OK' if 'OK' else 'NG'
print("'OK' if 'OK' else 'NG':", result5)

x = 1
result6 = 0 <= x <= 1
print("0 <= x <= 1:", result6)

result1 = [0, 1, 2] < [0, 1, 3]
print("[0, 1, 2] < [0, 1, 3]:", result1)

result2 = [0, [0, 1, 2]] < [0.0, [0, 1, 3]]
print("[0, [0, 1, 2]] < [0.0, [0, 1, 3]]:", result2)

result3 = 'abc' < 'abd'
print("'abc' < 'abd':", result3)
