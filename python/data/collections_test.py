#!env python3
# -*- coding: utf-8 -*-
from collections import Counter

# Counter
count = Counter(["apple", "melon", "orange", "apple", "orange", "apple"])
print(count)
print(count.most_common(2))
print(count.most_common(1))
