#!env python3
# -*- coding: utf-8 -*-
import csv

file = 'tmp.tsv';
with open(file, 'w') as fd:
    writer = csv.writer(fd, delimiter='\t')
    writer.writerow(["番号", "名称", "読み"])
    writer.writerow([1, "Python", "パイソン"])
    writer.writerow([2, "Java", "ジャバ"])
    writer.writerow([3, "JavaScript", "ジャバスクリプト"])
    writer.writerow([4, "Ruby", "ルビー"])

with open(file, 'r') as fd:
    reader = csv.reader(fd, delimiter='\t')
    for line in reader:
        print(line)

with open(file, 'r') as fd:
    reader = csv.DictReader(fd, delimiter='\t')
    for line in reader:
        for key in line:
            print(key, line[key], end=', ')
        print()

with open(file, 'w') as fd:
    fieldnames = ["番号", "名称", "読み"]
    writer = csv.DictWriter(fd, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    writer.writerow({"番号":1, "名称":"Python", "読み":"パイソン"})
    writer.writerow({"番号":2, "名称":"Java", "読み":"ジャバ"})     
    writer.writerow({"番号":3, "名称":"JavaScript", "読み":"ジャバスクリプト"})
    writer.writerow({"番号":4, "名称":"Ruby", "読み":"ルビー"})

