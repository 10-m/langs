#!env python3
# -*- coding: utf-8 -*-

here_document = '''aaa
bbb
ccc
'''
print(here_document)
for l in here_document.split('\n'):
    print(l)

message = 'Hello, World'
print(message[0])
print(message[7:])
print(message[2:4])
print(message[:5])
print(message[-1]) # 最後の文字
print(message[:-3])  # 最初から最後から3文字目
print(message[::2]) # ステップ, 2文字ごと
print(message[::-1]) # reverse

s = 'aaabbbccc'
if 'bbb' in s:
    print('include bbb')
if s.startswith('aaa'):
    print('startswith aaa')


bye = 'さようなら'
print(len(bye))
# number of bytes
print(len(bye.encode('utf-8')))

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

# translate
print("AabcD".translate(str.maketrans("abc", "ABC")))

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

# operator
s = 'pine' 'apple'
print(s)
s = ('pine'
     'apple')
print(s)
print('Yes' * 3)
print('is' in 'this')

# is method
print("'abc'.isalpha():", 'abc'.isalpha())
print("'ab3'.isalpha():", 'ab3'.isalpha())
print("'12'.isdigit():", '12'.isdigit())
print("'abc'.islower():", 'abc'.islower())
print("'ABC'.isupper():", 'ABC'.isupper())
print("'Abc'.isupper():", 'Abc'.isupper())
print("'Abc'.lower():", 'Abc'.lower())
print("'Abc'.upper():", 'Abc'.upper())

# find method
print("'ABCAB'.count('AB'):", 'ABCAB'.count('AB'))
print("'ABC'.find('X'):", 'ABC'.find('X'))
print("'ABC'.index('B'):", 'ABC'.index('B'))
print("'ABC'.endswith('BC'):", 'ABC'.endswith('BC'))
print("'ABC'.startswith('AB'):", 'ABC'.startswith('AB'))
print("'ABC'.startswith('BA'):", 'ABC'.startswith('BA'))
print("'ABC'.startswith(('AB', 'BA')):", 'ABC'.startswith(('AB', 'BA')))
print("'Abc'.swapcase()", 'Abc'.swapcase())

# transform method
print("'...'.splitlines()", """\
Alice
Bob
Carol""".splitlines())
print("'abcd'.replace('bc', '-'):", 'abcd'.replace('bc', '-'))
print("'1 2 3'.split():", '1 2 3'.split())
print("'1<>2<><><3'.split('<>'):", '1<>2<><><3'.split('<>'))
print("'--abc--'.strip('-'):", '--abc--'.strip('-'))
print("'--abc--'.rstrip('-'):", '--abc--'.rstrip('-'))
print("'--abc--'.lstrip('-'):", '--abc--'.lstrip('-'))
print("'-'.join('1 2 3'.split()):", '-'.join('1 2 3'.split()))
