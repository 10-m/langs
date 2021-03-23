#!env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

with open('item-list.html', 'r', encoding='utf-8') as f:
    html = f.read()

bs = BeautifulSoup(html, 'html.parser')
div_item_list = bs.select('div.item-list')
for div_item in div_item_list[0].select('div.item'):
    item_release_date = div_item.select('span.item-release-date')[0].text.strip()
    print(item_release_date)
