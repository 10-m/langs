#!env python3
# -*- coding: utf-8 -*-
import requests

response = requests.get("https://en.wikipedia.org/wiki/Nobel_Prize")
#print(dir(response))
print(response.status_code)
print(response.headers)
# print(response.text)

response = requests.get("http://maps.googleapis.com/maps/api/geocode/json?address=mt.fuji")
print(response.status_code)
data = response.json()
print(data.keys())
print(data['results'])
