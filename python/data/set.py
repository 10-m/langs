#!env python3
# -*- coding: utf-8 -*-

s1 = {"dog", "cat", "pig", "cow"}
print(s1)

s2 = set(["dog", "cat", "pig", "cow"])
print(s1)

# add
s1 = {"red", "green", "blue"}
s1.add("black")
print(s1)

# update
s1 = {"red", "green", "blue"}
s1.update(["black", "yellow"])
print(s1)

# operator
print({1, 4, 5} | { 4, 3, 20})
print({1, 4, 5} - { 4, 3, 20})
print({1, 4, 5} ^ { 4, 3, 20})
print({1, 2} <= {1, 2})
print({1, 2} <= {1, 2, 3})
print({4, 5, 6} > {4, 5, 6})
print({4, 5, 6} > {4, 5})

# remove
s1 = {"blue", "black", "red", "green"} 
s1.remove("blue")
print(s1)

# discard
s1 = {"blue", "black", "red", "green"} 
s1.discard("blue")
print(s1)
s1.discard("blue")
print(s1)

# pop
myset = {1965, 1959, 2001, 1987, 1959, 2011}
while True:
    try:
        print(myset.pop())
    except:
        break

# frozenset
s1 = {"green", "blue"} 
s2 = {"black", "white"} 
d1 = {frozenset(s1):3 , frozenset(s2):4} 
print(d1)

# copy
s1 = {"東京都", "神奈川県", "千葉県"} 
s2 = s1.copy()
s1.add("大阪府")
print(s1)
print(s2)
