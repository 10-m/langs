#!env python3
# -*- coding: utf-8 -*-
from enum import Enum
from datetime import date

class Wareki(Enum):
    大正 = 1
    昭和 = 2
    平成 = 3
    令和 = 4

print(Wareki.令和)
print(Wareki.令和.value)
print(Wareki.令和.name)
print(Wareki.令和 == 4)
print(Wareki.令和 == Wareki(4))

# 任意のオブジェクトを格納
class Wareki2(Enum):
    大正 = (1912, 7, 30)
    昭和 = (1926, 12, 25)
    平成 = (1989, 1, 8)
    令和 = (2019, 5, 1)

    def __init__(self, y, m, d):
        self.start_date = date(y, m, d)

print(Wareki2.令和.name)
print(Wareki2.令和.value)
print(Wareki2.令和.start_date)

# メソッドを追加
class Wareki3(Enum):
    大正 = (1912, 7, 30)
    昭和 = (1926, 12, 25)
    平成 = (1989, 1, 8)
    令和 = (2019, 5, 1)

    def __init__(self, y, m, d):
        self.start_date = date(y, m, d)

    @staticmethod
    def to_japanese_era(y, m, d):
        """西暦の年月日を和暦の年に."""
        input_date = date(y, m, d)
        for gengo in reversed(Wareki3):
            if input_date >= gengo.start_date:
                n = y - gengo.start_date.year + 1
                return f'{gengo.name}{n if n > 1 else "元"}年'
        raise ValueError('大正以前')

print(Wareki3.to_japanese_era(2019, 4, 30))  # 平成31年
print(Wareki3.to_japanese_era(2019, 5, 1))  # 令和元年
