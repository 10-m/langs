#!env python3
import multiprocessing
import os
import random
import time
from datetime import datetime
from datetime import timedelta

date_format = '%Y/%m/%d'
with open("today.txt", 'wt') as fh:
    now = time.localtime()
    fh.write(time.strftime(date_format, now))

with open("today.txt", 'rt') as fh:
    text = fh.read()
    date = time.strptime(text, date_format)
    print(date.tm_year, date.tm_mon, date.tm_mday)

for file in os.listdir('.'):
    print(file)

for file in os.listdir('..'):
    print(file)

birthday = datetime.strptime('2018/7/19', date_format)
print(birthday.strftime('%a'))

elapsed = timedelta(days=10000)
print((birthday + elapsed).strftime(date_format))

def my_sleep(sec):
    print(sec)
    time.sleep(sec)

procs = []
for n in range(3):
    t = random.randrange(1, 6)
    proc = multiprocessing.Process(target=my_sleep, args=[t])
    proc.start()
    procs.append(proc)

[proc.join() for proc in procs]
