import requests
import time
import datetime
import re #正则表达式
from bs4 import BeautifulSoup
import levtechDao

levtechDao.create_db()
# 写网站站点
url = "https://freelance.levtech.jp/"
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
# 案件总数
total = int(soup.find(id="topSearchCount").string)
# 打印片名
print(total)
# 现在时间
date = datetime.datetime.now()
print("存储案件总数为%s"%total)
levtechDao.insert_total(date,total)
print("存储成功")
# data
data = soup.find(class_='searchTab__body')
# 语言
linkArrow = data.find_all(class_='linkArrow')
# 语言案件数
searchLinkList__item__sub = data.find_all(class_='searchLinkList__item__sub')
for i in range(len(linkArrow)):
 language = linkArrow[i].string
 languageCount = int(searchLinkList__item__sub[i].string.replace('(', '').replace('件)', '')) 
 print("语言：%s\n案件数：%s"% (language,str(languageCount)))
 levtechDao.insert_language(date,language,languageCount)
print("存储成功")