#!env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

BASE_URL = 'http://en.wikipedia.org'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def get_Nobel_soup():
    """ ノーベル賞ページの解析したタグツリーを返す """
    # 有効な header を設定してノーベル賞ページにリクエストを行う
    response = requests.get(
        BASE_URL + '/wiki/List_of_Nobel_laureates', headers=HEADERS)
    # BeautifulSoup が解析したレスポンスの内容を返す
    return BeautifulSoup(response.content, "lxml")

soup = get_Nobel_soup()
# print(soup.find('table', {'class':'wikitable sortable'}))
# print(soup.select('table.sortable.wikitable'))

table = soup.select_one('table.sortable.wikitable')
# print(table.select('th'))

def get_column_titles(table):
    """ テーブルヘッダからノーベル賞分野を取得する """
    cols = []
    for th in table.select_one('tr').select('th')[1:]:  # ?
        link = th.select_one('a')
        # 分野名と Wikipedia リンクを格納する
        if link:
            cols.append({'name':link.text,\
                         'href':link.attrs['href']})
        else:
            cols.append({'name':th.text, 'href':None})
    return cols

print(get_column_titles(table))
