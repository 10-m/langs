#!env python3
# -*- coding: utf-8 -*-

import requests
import requests_cache

requests_cache.install_cache()

requests_cache.install_cache('nobel_pages', expire_after=7200)
response = requests.get("https://en.wikipedia.org/wiki/Nobel_Prize")
