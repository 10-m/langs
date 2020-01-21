#!env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
import calendar

# コンストラクタ
t = datetime(2017, 11, 22)
print(t)
print(datetime(2016, 5, 5, 14, 15, 30))


# isoformat
print(t.isoformat())

# timetuple
print(t.timetuple())

# weekday
print(t.weekday())

c = calendar.TextCalendar()
print(c.formatmonth(2017,11))

# now
now = datetime.now()
datestr = '{0:%Y}年{0:%m}月{0:%d}日'.format(now)
print(datestr)
timestr = '{0:%p} {0:%I}時{0:%M}分'.format(now)
print(timestr)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# today
print(datetime.today())

# time
d = datetime(2000,1,1,hour=12, minute=34, second=56) 
print(d.hour)
print(d.minute)
print(d.second)
print(d.microsecond)

# strptime
str_day = '1600/10/21'
one_day = datetime.strptime(str_day, '%Y/%m/%d')
print(one_day)

# strftime
print(one_day.strftime('%Y-%m-%d'))

# 経過
birthday = datetime(1992, 12, 15)
today = datetime.today()
newcentury = datetime(2100, 1, 1)
elapsed0 = newcentury - today
elapsed1 = today - birthday
days0 = elapsed0.days
days1 = elapsed1.days
print("{0} days to new century".format(days0))
print("You have lived {0} days so far".format(days1))

# timedelta
print(datetime.now() - timedelta(days=2))
print(datetime.now() > (datetime.now() - timedelta(days=2)))
