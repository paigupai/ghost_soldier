import requests
import time
import re #正则表达式
import sqlite3

con = sqlite3.connect('smzdm.sqlite')
cur = con.cursor()
cur.execute('CREATE TABLE novel ("novel_name" TEXT,"title" TEXT);')
sql = "insert into novel(novel_name,title) values(?,?)"
# 写网站站点
url = "http://www.jingcaiyuedu.com/novel/GLSmM4.html"
# 写入headers模拟浏览器上网,避免出现个别网站拒绝访问的情况
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",}
# get发送请求
response = requests.get(url,headers=headers)
# 将网页编码方式转换为utf-8
response.encoding = 'utf-8'
# 网站源码
html = response.text
# re.findall获取小说的名字
novel_name = re.findall(r'<meta property="og:title" content="(.*?)"/>',html)[0]
# 打印小说的名字
print(novel_name)
# 获取每一章的信息(章节的url)
dl = re.findall(r'<dl class="panel-body panel-chapterlist">.*?</dl>',html,re.S)[1]
aill = re.findall(r'href="(.*?)">(.*?)<',dl)
# 循环每一个章节,分别去下载
for i in aill:
# 反爬
 #time.sleep(1)
# 章节地址和名
 book_url,book_name = i
 print("存储"+book_name)
 title = book_name
 cur.execute(sql, [novel_name, title])
 con.commit()
 print("存储成功")
con.close()
print("终了")