#!env python3
# -*- coding: utf-8 -*-

## initalize

s1 = {"dog", "cat", "pig", "cow"}
print(s1)

# from list
s2 = set(["dog", "cat", "pig", "cow"])
print(s1)

# from tuple
s3 = set(('A', 'B', 'C', 'C'))
print(s3)

# empty
print(set())

## method
# add
s1 = {"red", "green", "blue"}
s1.add("black")

# add tuple
s1.add(('white', 'purple'))
print(s1)

# update
s1 = {"red", "green", "blue"}
s1.update(["black", "yellow"])
print(s1)

# remove。指定した要素が無いときはKeyError
s1 = {"blue", "black", "red", "green"} 
s1.remove("blue")
print(s1)

# discard。指定した要素が無いときはKeyErrorにならない
s1 = {"blue", "black", "red", "green"} 
s1.discard("blue")
print(s1)
s1.discard("blue")
print(s1)

# pop
myset = {1965, 1959, 2001, 1987, 1959, 2011}
while myset:
    print(myset.pop())

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

## operator
print({1, 4, 5} & { 4, 3, 20}) # s1.intersection(s2)
print({1, 4, 5} | { 4, 3, 20}) # s1.union(s2)
print({1, 4, 5} - { 4, 3, 20}) # s1.difference(s2)
print({1, 4, 5} ^ { 4, 3, 20}) # s1.symmetric_difference(s2)
print({1, 2} <= {1, 2}) # 左辺の要素全てが右辺の集合に含まれているか
print({1, 2} <= {1, 2, 3})
print({4, 5, 6} > {4, 5, 6})# 左辺は右辺の部分集合か (完全一致は除く)
print({4, 5, 6} > {4, 5})
