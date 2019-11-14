# 引入库
import requests
import time
import re #正则表达式
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
title = re.findall(r'<meta property="og:title" content="(.*?)"/>',html)[0]
# 打印小说的名字
print(title)
# 获取每一章的信息(章节的url)
dl = re.findall(r'<dl class="panel-body panel-chapterlist">.*?</dl>',html,re.S)[1]
aill = re.findall(r'href="(.*?)">(.*?)<',dl)
# 新建文件保存小说内容
f = open(f"{title}.txt",'w',encoding="utf-8")
# 循环每一个章节,分别去下载
for i in aill:
# 反爬
 time.sleep(1)
# 章节地址和名
 book_url,book_name = i
# 正确章节地址http://www.jingcaiyuedu.com/novel/GLSmM4/1.html
# 拼接正确章节地址
 book_url = f"http://www.jingcaiyuedu.com{book_url}"
# 获取章节
 book_response = requests.get(book_url,headers=headers)
 book_response.encoding = 'utf-8'
 book_html = book_response.text
 if len(re.findall(r'<div class="panel-body" id="htmlContent">(.*?)</div>',book_html,re.S)) == 0:
     print(book_name + 'NULL')
     continue
# 提取章节内容
 book_content = re.findall(r'<div class="panel-body" id="htmlContent">(.*?)</div>',book_html,re.S)[0]
# 清洗提取的数据
 book_content = book_content.replace(' ','')
# 将其中内容的空格部分替换成空
 book_content = book_content.replace('&nbsp;','')
# 将其中内容的&nbsp;部分替换成空
 book_content = book_content.replace('<br />','')
# 将其中内容的<br />部分替换成空
 book_content = book_content.replace('<br/>','')
# 将其中内容的<br/>部分替换成空
# 写入
 f.write(f"{book_name}\n")
 print(book_name)
 f.write(f"{book_content}\n")
 f.write("\n")
 print(book_url)