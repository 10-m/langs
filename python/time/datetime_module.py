#!env python3
# -*- coding: utf-8 -*-
from datetime import date, time, datetime, timedelta
import calendar

## date
d = date(2019, 6, 7)
print(d)  # 2019-06-07
print(d.weekday())  # 4
print(d.year)  # 2019
print(d.month)  # 6
print(d.day)  # 7
print(f'{d:%Y/%m/%d}')

## time
tm = time(23, 45, 59)
print(tm)  # 23:45:59
print(tm.hour)
print(tm.minute)
print(tm.second)
print(f'{tm:%H:%M:%S}')  # 23:45:59

## datetime
dt = datetime(2019, 6, 7, 23, 45, 59)
print(dt.date())  # 2019-06-07
print(dt.day)  # 7
print(dt.hour)  # 23
print(f'{dt:%Y-%m-%d %H:%M:%S}')  # 2019-06-07 23:45:59
print(dt.isoformat())
print(dt.timetuple())
print(dt.weekday())
print(datetime.today())

## calendar
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

## timedelta
print(datetime.now() - timedelta(days=2))
print(datetime.now() > (datetime.now() - timedelta(days=2)))
