#!env python3
# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://google.com/')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

# Object Types
content = '<p class="text">Click to learn more about each turtle</p>'
soup = BeautifulSoup(content, "html.parser")
print(soup.p)
print(soup.p.string)

content = '''
<ul>
  <li class="banner"> 1 cup flour </li>
  <li class="banner", id="abc"> 1/2 cup sugar </li>
  <li> 2 tbsp oil </li>
  <li> 1/2 tsp baking soda </li>
  <li> ? cup chocolate chips </li> 
  <li> 1/2 tsp vanilla <li>
  <li> 2 tbsp milk </li>
</ul>
'''
content = content.rstrip()
soup = BeautifulSoup(content, "html.parser")
for child in soup.ul.children:
    print(child)

for parent in soup.ul.parents:
    print(parent)

# Find All
print(soup.find_all("li"))
print(soup.find_all(re.compile('u?li?')))
print(soup.find_all(['ul' , 'li']))
print(soup.find_all(attrs={'class':'banner'}))
print(soup.find_all(attrs={'class':'banner', 'id':'abc'}))
print(soup.find_all(lambda tag: tag.has_attr('class') and tag.attrs['class'][0] == 'banner'))

# CSS selecter
print(soup.select('.banner'))

# reading text
content = '''
<h1 class="results">Search Results for: <span class='searchTerm'>Funfetti</span></h1>
'''
soup = BeautifulSoup(content, "html.parser")
print(soup.get_text())
print(soup.get_text('|'))
