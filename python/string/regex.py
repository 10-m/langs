#!env python3
# -*- coding: utf-8 -*-
import re

# search
s = "Good 2018 Word"
p = "2..8"
if re.search(p, s):
    print('found ', p)

# match 先頭でマッチするか
s = "Bad News" 
print(re.search("News", s)) # match

print(re.match("News", s)) # not match
print(re.match("Bad", s)) # match

# group
m = re.search("P....n", "Hello Python") 
print(m.group())
print(m.start())
print(m.end())
print(m.span())

# raw
print(re.search("\bHello\b", "Hello World"))
print(re.search("\\bHello\\b", "Hello World"))
print(re.search(r"\bHello\b", "Hello World"))

# 最短マッチ
print(re.search("^.+,", "東京,大阪,名古屋,神戸").group())
print(re.search("^.+?,", "東京,大阪,名古屋,神戸").group())

# マッチオプジェクト
m = re.search("(.+),(.+),(.+)", "山田一郎,15,男性")
print(m.group(1))
print(m.group(2))
print(m.group(3))

# findall
print(re.findall(r"\b19\d\d\b", "2003, 1959, 1930, 1943, 2001"))

# finditer
itr = re.finditer(r"\b(.+?)曜日,?", "月曜日, 火曜日, 木曜日, 金曜日")
for m in itr:
    print(m.group(1))
    print("範囲:", m.span(1))

# split
s = "田無駅,  花小金井駅\t  ,新宿駅   小平駅  "
for st in re.split("[\s,]+", s):
    print(st)

# sub
print(re.sub("^hello", "Hello", "hello hello hello"))

# 後方参照
for person in ["山田太郎:45:男性", "中田功:34:男性", "山本洋子:25:女性"]:
    print(re.sub(r"(\w+):(\d+):(\w+)", r"\1:\3:\2", person))

# compile
people = ["山田太郎:45:男性", "中田功:34:男性",
          "山本洋子:25:女性",  "井上花子:23:女性"]
p = re.compile(":男性$")
for person in people:
    m = p.search(person)
    if m:
        print(person)
