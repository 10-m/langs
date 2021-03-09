#!env python3
# -*- coding: utf-8 -*-
import requests

response = requests.get("https://github.com", verify=False)
response.encoding = response.apparent_encoding
print(response.text)
