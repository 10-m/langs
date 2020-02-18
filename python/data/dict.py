#!env python3
# -*- coding: utf-8 -*-

# get
langs = {"Python":105, "JavaScript":20, "Swift":3, "Basic":5, "C":33}
l = langs.get('Objective-C')
print(l)
print(type(l))

# setdefault
l = langs.setdefault('Objective-C', 100)
print(l)

# update
d1 = {"yellow":"黄", "red":"赤"} 
d2 = {"blue":"青", "green":"緑"} 
d1.update(d2)
print(d1)

# del
langs = {"Python":105, "JavaScript":20, "Swift":3, "Basic":5, "C":33}
del langs['Basic']
print(langs)

# pop
langs = {"Python":105, "JavaScript":20, "Swift":3, "Basic":5, "C":33}
langs.pop('Basic')
langs.pop('Basic', None)

# popitem
langs = {"Python":105, "JavaScript":20, "Swift":3, "Basic":5, "C":33}
while langs:
    print(langs.popitem())

# keys, values, items
langs = {"Python":105, "JavaScript":20, "Swift":3, "Basic":5, "C":33}
print(list(langs.keys()))
print(list(langs.values()))
print(tuple(langs.items()))

# sort by value
for l, v in sorted({"Python":105, "JavaScript":20, "Swift":3, "Basic":5, "C":33}.items(), key=lambda l:l[1]):
    print(l, v)

# copy
langs1 = {"Python":105, "JavaScript":20, "Swift":3, "Basic":5, "C":33}
langs2 = langs1
langs3 = langs1.copy()
langs1["Python"] = 2000
print(langs2)
print(langs3)

# clear
langs3.clear()
print(langs3)
