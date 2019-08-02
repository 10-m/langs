#!env python3
# -*- coding: utf-8 -*-
import datetime
import calendar

# コンストラクタ
t = datetime.date(2017, 11, 22)
print(t)

# isoformat
print(t.isoformat())

# timetuple
print(t.timetuple())

# weekday
print(t.weekday())

c = calendar.TextCalendar()
print(c.formatmonth(2017,11))

# now
now = datetime.datetime.now()
datestr = '{0:%Y}年{0:%m}月{0:%d}日'.format(now)
print(datestr)
timestr = '{0:%p} {0:%I}時{0:%M}分'.format(now)
print(timestr)

# today
print(datetime.date.today())

# time
d = datetime.time(12, 34, 56) 
print(d.hour)
print(d.minute)
print(d.second)
print(d.microsecond)

# 経過
birthday = datetime.date(1992, 12, 15)
today = datetime.date.today()
newcentury = datetime.date(2100, 1, 1)
elapsed0 = newcentury - today
elapsed1 = today - birthday
days0 = elapsed0.days
days1 = elapsed1.days
print("{0} days to new century".format(days0))
print("You have lived {0} days so far".format(days1))
