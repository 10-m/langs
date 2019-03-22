#!env python3
# -*- coding: utf-8 -*-
import string

bye = 'さようなら'
print(len(bye))
# number of bytes
print(len(bye.encode('utf-8')))

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

# strip
print('\naaa '.strip())
print(',aaa...'.strip(',.'))
print('<aaa>'.lstrip('<>'))
print('<aaa>'.rstrip('<>'))

# join
print(','.join(['a', 'b', 'c']))

# str
print(str(255))
print(str(0xff))
print(str(0b11111111))

# 2, 8, 16進数
print(bin(255))
print(oct(255))
print(hex(255))

# int
print(int('123'))
print(int('ff', 16))

# float
print(float('3.14'))

# isxxxx
print('hello1234'.isalnum())
print('2017'.isdecimal())
print('\u00B2'.isdecimal())
print('\u00B2'.isdigit())
print('四'.isdecimal())
print('四'.isnumeric())
print('ⅠⅩ'.isdigit())
print('ⅠⅩ'.isnumeric())
print(' \n\t'.isspace())

# split
print('a<>b<>c'.split('<>'))

# splitlines
print('a\nb\nc'.splitlines())

# ljust, center, rjust, zfill
print('Python'.ljust(10))
print('Python'.ljust(10, '-'))
print('Python'.center(10))
print('Python'.rjust(10))
print('123'.zfill(6))
print('+123'.zfill(6))
print('-123'.zfill(6))

# encode, decode
utf8 = 'こんにちは'.encode()
sjis = 'こんにちは'.encode(encoding="shift-jis")
print(utf8)
print(sjis)
print(utf8.decode())
print(sjis.decode(encoding="shift-jis"))

# ord, chr
print(ord('a'))
print(chr(ord('a')))

# epandtab
print("Hi\tLow\tGood\tOK".expandtabs())
print("Hi\tLow\tGood\tOK".expandtabs(tabsize=4))
