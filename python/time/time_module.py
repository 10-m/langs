#!env python3
# -*- coding: utf-8 -*-

import time
import timeit

# エポック秒
print(time.time())
print(time.ctime())

# localtime
t = time.localtime()
print("year={0} month={1} day={2}".format(t.tm_year, t.tm_mon, t.tm_mday))
print("year={0} month={1} day={2}".format(t[0], t[1], t[2]))

# sleep
time.sleep(0.5)

# timeit
print(timeit.timeit("for i in range(1000): total+=i", "total=0", number=10000))
t = timeit.Timer("math.sin(10)", "import math") 
print(t.timeit())
