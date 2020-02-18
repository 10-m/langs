#!env python3
# -*- coding: utf-8 -*-

# unpack for tuple
python = ('Python', 1991)
ruby = ('Ruby', 1995)
go = ('Go', 2009)

programming_lang = (python, ruby, go)

for lang in programming_lang:
    name, year = lang
    print(name, year)

a, b, c = programming_lang
print(a, b, c)
a, *b = programming_lang
print(a, b)

# use tuple as key for dict
tuple_key_dict = {(1, 2): 'A'}
print(tuple_key_dict[(1, 2)])
