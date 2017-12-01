#!env python3
# -*- coding: utf-8 -*-

from datetime import datetime

d = datetime.now()
print(d.isoformat())

d = datetime.strptime('2015-09-15 21:48:50', '%Y-%m-%d %H:%M:%S')
print(d)
