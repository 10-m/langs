#!env python3
# -*- coding: utf-8 -*-
from collections import Counter, defaultdict

# Counter
count = Counter(["apple", "melon", "orange", "apple", "orange", "apple"])
print(count)
print(count.most_common(2))
print(count.most_common(1))

# defaultdict
people = ((20,"Taro"),(23,"Ken"),(21,"Rin"),(20,"Joe"),(22,"Risa"))
d = defaultdict(list)
for age, name in people:
    d[age].append(name)
print(d)

