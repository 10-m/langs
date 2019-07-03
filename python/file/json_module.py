#!env python3
# -*- coding: utf-8 -*-
import json

data = {'customers':[
            {'name': '井上三郎', 'age': 45, 'mail': 'save@example.com'},
            {'name': '田中花子', 'age': 51, 'mail': 'hanar@example.com'},
            {'name': '江藤真', 'age': 23, 'mail': 'makoto2@example.com'}]}

file = 'tmp.json';
with open(file, 'w', encoding="utf-8") as fd:
    json.dump(data, fd, ensure_ascii=False, indent=4)

with open(file, 'r', encoding="utf-8") as fd:
    json_obj = json.load(fd)
    print(json_obj)

json_str = json.dumps(data, ensure_ascii=False, indent=4)
print(json_str)

json_obj = json.loads(json_str)
print(json_obj)
