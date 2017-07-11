#!env python3
# -*- coding: utf-8 -*-

class MonthName:
    month = [""] * 12
    month[0:2] = ["Jan", "Feb", "Mar"]
    def __getitem__(self, key):
        i = int(key)
        return self.month[i - 1]
    def __setitem__(self, key, value):
        i = int(key)
        if (i < 1) or (i > 12):
            raise ValueError("out of range")
        else:
            self.month[i - 1] = value

m = MonthName()
print(m[1])
print(m[2])
print(m[3])
m[4] = "Apr"
print(m[4])
