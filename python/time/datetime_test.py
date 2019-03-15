#!env python3
# -*- coding: utf-8 -*-
from datetime import datetime

now = datetime.now()
datestr = '{0:%Y}年{0:%m}月{0:%d}日'.format(now)
print(datestr)
timestr = '{0:%p} {0:%I}時{0:%M}分'.format(now)
print(timestr)
