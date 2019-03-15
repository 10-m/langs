#!env python3
# -*- coding: utf-8 -*-

str = 'さようなら'
print(len(str))
# number of bytes
print(len(str.encode('utf-8')))

# repeat string
print('hello' * 3)

# upper, lower, swapcase
print('Abc'.upper())
print('Abc'.lower())
print('Abc'.swapcase())

# slice
print('abcd'[0]) # a
print('abcd'[1]) # b
print('abcd'[-1]) # d
print('abcd'[-2]) # c
print('abcd'[:2]) # ab
print('abcd'[1:3]) # bc
print('abcd'[3:]) # d
print('sample.txt'[:-4]) # sample
print('0123456789'[::2]) # 02468
print('0123456789'[::-1]) # 9876543210

# replace
print("good new good new good".replace("good", "bad"))
print("good new good new good".replace("good", "bad", 2))

# translate
print("AabcD".translate(str.maketrans("abc", "ABC")))

# count
print("good bad good".count("good"))

# format
print('{}, {}, {}'.format('one', 'two', 'three'))
print('{1}, {2}, {0}'.format('one', 'two', 'three'))
print('{0}, {0}, {0}'.format('one', 'two', 'three'))
urldata = {"scheme":"http","netloc":"qiita.com","path":"/drafts"}
print("{scheme}://{netloc}{path}".format(**urldata))

# f string
doller = 5
rate = 108
yen = 110
print(f'{doller} {doller * rate}')
print(f'{doller/100:.2%}')
