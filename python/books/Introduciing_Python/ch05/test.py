#!env python3
# -*- coding: utf-8 -*-

import collections
from collections import defaultdict

plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)

fancy = collections.OrderedDict({'a': 1, 'b': 2, 'c': 3})
print(fancy)

dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something  for a')
print(dict_of_lists['a'])
