import requests
import time
import re #正则表达式
import sqlite3
from bs4 import BeautifulSoup

con = sqlite3.connect('acfun.sqlite')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS gohst_soldier ( "date" dateTIME NOT NULL, "name" TEXT NOT NULL, "clicks" INTEGER, "clisksIncrease" INTEGER, "totalDanmaku" INTEGER, "danmakuIncrease" INTEGER, "totalRating" INTEGER, "ratingIncrease" INTEGER, PRIMARY KEY("date","name") );')
sql = "insert into gohst_soldier(date,name,clicks,clisksIncrease,totalDanmaku,danmakuIncrease,totalRating,ratingIncrease) values(?,?,?,?,?,?,?,?)"
# 写网站站点
url = "https://www.acfun.cn/bangumi/aa6000218"
# 写入headers模拟浏览器上网,避免出现个别网站拒绝访问的情况
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",}
# get发送请求
response = requests.get(url,headers=headers)
# 将网页编码方式转换为utf-8
response.encoding = 'utf-8'
# 网站源码
html = response.text
# lxml化
soup = BeautifulSoup(html,'lxml')
# 片名
name = soup.find('h1',class_='title').find('a').string
# 打印片名
print(name)
# title
title = soup.find('h1',class_='title').get_text(strip=True).replace('\xa0','')
# 打印片名
print(title)
data = soup.find('div',class_='report-bar bangumi')
# 点击
clicks = data.find('span',class_='view fl').find('span',class_='sp2').string
# 弹幕
danmaku = data.find('span',class_='danmu fl').find('span',class_='sp2').string
# 评论
rating = data.find('span',class_='comm fl').find('span',class_='sp2').string
print(clicks,danmaku,rating)