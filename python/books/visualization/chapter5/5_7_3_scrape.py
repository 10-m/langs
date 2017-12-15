#!env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import requests_cache
import re

requests_cache.install_cache('nobel_pages',\
                             backend='sqlite', expire_after=7200)

def get_winner_nationality(w):
    """ 受賞者の Wikipedia ページから人物情報データをスクレイピングする """
    data = requests.get('http://en.wikipedia.org' + w['link'])
    soup = BeautifulSoup(data.content, 'lxml')
    person_data = {'name': w['name']}
    attr_rows = soup.select('table.infobox tr')  # ?
    for tr in attr_rows:  # ?
        try:
            attribute = tr.select_one('th').text
            if attribute == 'Nationality':
                person_data[attribute] = tr.select_one('td').text
        except AttributeError:
            pass
    return person_data

def get_Nobel_winners(table):
    cols = get_column_titles(table)
    winners = []
    for row in table.select('tr')[1:-1]:
        m = re.match(row.select_one('td').text, r'^(\d+)')
        year = int(re.match(r'^(\d+)', row.select_one('td').text).group(1))
        for i, td in enumerate(row.select('td')[1:]):
            for winner in td.select('a'):
                href = winner.attrs['href']
                if not href.startswith('#endnote'):
                    winners.append({
                        'year': year,
                        'category': cols[i]['name'],
                        'name': winner.text,
                        'link': winner.attrs['href']
                    })
    return winners

BASE_URL = 'http://en.wikipedia.org'
# httpheader に「User-Agent」属性を追加しないと、
# Wikipedia はリクエストを拒否する
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def get_Nobel_soup():
    """ ノーベル賞ページの解析したタグツリーを返す """
    # 有効な header を設定してノーベル賞ページにリクエストを行う
    response = requests.get(
        BASE_URL + '/wiki/List_of_Nobel_laureates', headers=HEADERS)
    # BeautifulSoup が解析したレスポンスの内容を返す
    return BeautifulSoup(response.content, "lxml")
    
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

soup = get_Nobel_soup()
table = soup.select_one('table.sortable.wikitable')
winners = get_Nobel_winners(table)

wdata = []
# 最初の 50 人の受賞者を調べる
for w in winners[:50]:
    wdata.append(get_winner_nationality(w))
missing_nationality = []
for w in wdata:
    # 「Nationality」が欠けていればリストに追加する
    if not w.get('Nationality'):
        missing_nationality.append(w)
# リストを出力する
print(missing_nationality)
