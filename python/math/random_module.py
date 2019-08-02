#!env python3
# -*- coding: utf-8 -*-

import random

# randrange : integer
print(random.randrange(1, 7)) # 1 to 6

# random
print(random.random())

# uniform
print(random.uniform(1, 100))

# normalvariate
# （μ、σ）の正規分布に従った乱数を返す
print(random.normalvariate(50,10))

# triangular
# low 以上、high 以下で、modeを最頻値とする乱数
print(random.triangular(0,100,50))

# betavariate
# パラメータα、βで表されるベータ分布
print(random.betavariate(0.5, 0.5))

# choice
seasons = ["Spring", "Summer", "Autumn", "Winter"]
print(random.choice(seasons))

# shuffle
random.shuffle(seasons)
print(seasons)

# sample
print(random.sample(seasons, 2))


