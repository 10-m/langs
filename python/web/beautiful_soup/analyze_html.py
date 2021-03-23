#!env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

html = '''
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title> test </title>
  </head>
  <body>
    <h1>test h1</h1>
    <ul id="link-list">
      <li>
        <a href="http://example.com/1">test1</a>
      </li>
      <li>
        <a href="http://example.com/2">test2</a>
      </li>
      <li>
        <a href="http://example.com/3">test3</a>
      </li>
    <ul>
  </body>
</html>

'''

bs = BeautifulSoup(html, "html.parser")


ul_tag = bs.find('ul')

# ulタグの中のaタグ
for a_tag in ul_tag.find_all('a'):

    # aタグのテキスト
    text = a_tag.text

    # aタグのhref属性
    link_url = a_tag['href']

    print('{}: {}'.format(text, link_url))
