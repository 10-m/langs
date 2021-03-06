#!env python3
# -*- coding: utf-8 -*-

lst = [1, 2, 3, 4]
print('lst:', lst)
print('lst[0]:', lst[0])
print('lst[-1]:', lst[-1])

# slice
print('lst[1:3]:', lst[1:3])
print('lst[1:]:', lst[1:])
print('lst[:2]:', lst[:2])
print('lst[1::2]:', lst[1::2])
print('lst[:0:-1]:', lst[:0:-1])

# operator
print('lst + [5, 6]:', lst + [5, 6])
print('lst * 2:', lst * 2)

# modify, append
lst = [1, 2, 3, 4]
print('lst:', lst)
lst[0] = 10
lst[1:4] = 20, 30
print('lst:', lst)
lst.append(40)
print('lst:', lst)

# insert
lst = [1, 2, 3, 4]
lst.insert(1, 100)
print('lst:', lst)

# pop
numbers = [100, 200, 300, 400, 500]
# 末尾を削除
print(numbers.pop())
print(numbers)

# 2番目の要素の削除
numbers.pop(1)
print(numbers)
