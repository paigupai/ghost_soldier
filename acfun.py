import requests
import time
import datetime
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
# urlList
urlList = []
for a in soup.find('ul',class_='videoes active').find_all('li'):
 print(a['data-href'])
 urlList.append(a['data-href'])
# 打印urlList
print(urlList)
data = soup.find('div',class_='report-bar bangumi')
# 总点击
allClicks = data.find('span',class_='view fl').find('span',class_='sp2').string
# 总弹幕
allDanmaku = 0
# 总评论
allRating = 0
for episodeURL in urlList:
# 反爬
 #time.sleep(1)
 # 拼接正确地址
 episode_url = "https://www.acfun.cn" + episodeURL
 print(episode_url)
# 获取章节
 episode_response = requests.get(episode_url,headers=headers)
 episode_response.encoding = 'utf-8'
 episode_html = episode_response.text
 # lxml化
 episode_soup = BeautifulSoup(episode_html,'lxml')
 episode_data = episode_soup.find('div',class_='report-bar bangumi')
 # 每话弹幕
 danmaku = episode_data.find('span',class_='danmu fl').find('span',class_='sp2').string
 # 总弹幕数字
 if danmaku == "...":
    allDanmaku = allDanmaku + 0
 else:
    allDanmaku = allDanmaku + int(danmaku) 
 # 每话评论
 rating = episode_data.find('span',class_='comm fl').find('span',class_='sp2').string
 # 总评论数字
 allRating = allRating + int(rating.replace(',', '')) 
date = datetime.datetime.now()
if '万' in allClicks:
 clicks = int(float(allClicks.replace('万', ''))*10000)
print("检查DB")
cur.execute("SELECT COUNT(*) from gohst_soldier")
count=cur.fetchone()
print(count)
#上回的数值
last_clisks = 0
last_danmaku = 0
last_rating = 0
if len(count) >0:
 print("取得上回的数值")
 cur = cur.execute("select * from 'gohst_soldier' order by date desc limit 1;")
 for row in cur:
   last_clisks = row[2]
   print("last_clisks = ", row[2])
   last_danmaku = row[4]
   print("last_danmaku = ", row[4])
   last_rating = row[6]
   print("last_rating = ", row[6])
clisksIncrease = clicks - last_clisks
danmakuIncrease = allDanmaku - last_danmaku
ratingIncrease = allRating - last_rating
print("开始新规存储")
cur.execute(sql, [date,name,clicks,clisksIncrease,allDanmaku,danmakuIncrease,allRating,ratingIncrease])
con.commit()
print("存储成功")
con.close()
print("终了")
print(clicks,allDanmaku,allRating)