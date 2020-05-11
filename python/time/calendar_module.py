#!env python3
# -*- coding: utf-8 -*-

import calendar

# 閏年
print(calendar.isleap(2019))  # False
print(calendar.isleap(2020))  # True

# 曜日（0は月曜日）
print(calendar.weekday(2019, 5, 1))  # 2

# 月の一日の曜日と月の日数
print(calendar.monthrange(2019, 5))  # (2, 31)

# 月の晦日（月末）の曜日
print((sum(calendar.monthrange(2019, 5)) - 1) % 7)  # 4

# 該当月のカレンダーを表示
print(calendar.prmonth(2019, 1))

# 該当年のカレンダーを表示
# print(calendar.prcal(2019))
