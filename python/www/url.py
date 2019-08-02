#!env python3
# -*- coding: utf-8 -*-

import urllib.parse

# urlparse
r = urllib.parse.urlparse("https://www.impress.co.jp/business.html;hoge=1;?say=hello#01_digital")
print(r)

# urljoin
from urllib.parse import urljoin
a = urljoin("http://www.impress.co.jp", "whatsup.html")
print(a)
b = urljoin("http://www.impress.co.jp/news/", "../weather/index.html")
print(b)
c = urljoin("http://www.impress.co.jp/search?key=hello", "../images/logo.png")
print(c)

# quote
r = urllib.parse.quote("あいう")
print(r)

# unquote
print(urllib.parse.unquote(r))

# urlencode
print(urllib.parse.urlencode({'ja': "はい", 'en': 'Yes'}))
