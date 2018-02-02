#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 17:25:37 2018

@author: shockwave
"""
from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "http://www.imdb.com/india/top-rated-indian-movies/"
html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.content, 'html.parser')
titinfo = soup.find_all("td", {"class": "titleColumn"})
names = [];links = [];years = []
colR = soup.find_all("td", {"class": "ratingColumn imdbRating"})
rated = []
for i in titinfo:
    k = i.find("a")
    links.append("www.imdb.com"+k.get('href').encode('ascii'))
    
    
    names.append(k.get_text().encode('ascii'))
    
    j = i.find("span", {"class": "secondaryInfo"})
    years.append(j.get_text().encode('ascii'))


for j in colR:
    n = j.find("strong")
    rated.append(n.get_text().encode('ascii'))
    
        
data = {'Movie_Name': names,'Year': years,'Rating': rated,'Link': links}
f=pd.DataFrame(data, columns=['Movie_Name','Year','Rating','Link'] )
print "*****************IMDB TOP 250 INDIAN MOVIES INFO*********************"
print f


dir="IMDBdata.csv"
fo = open(dir, "w")
 
for i in range(len(names)):
    row = names[i] + "," + years[i] + "," + rated[i] + "," + links[i] + "\n"
    fo.write(row)

