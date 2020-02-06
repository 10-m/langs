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

print(','.join(['A', 'B', 'C']))
print('aabbcc'.replace('bb', 'BB'))
print(len('aaa'))

s = 'aaabbbccc'
if 'bbb' in s:
    print('include bbb')
if s.startswith('aaa'):
    print('startswith aaa')
