import requests
import re 
from bs4 import BeautifulSoup
import bilibili_url_search_DB
import threading



max = 100000
nowNum = 0
erroNum = 0

lock = threading.Lock()

bilibili_url_search_DB.create_db()

def printTitle():
 global max,nowNum,erroNum
 while True:
  if nowNum  == max:
      break
   # 请求锁
  lock.acquire()
  nowNum += 1
  # 释放锁
  lock.release()  
# 写网站站点
  url = "https://www.bilibili.com/bangumi/play/ss" + str(nowNum)
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
  print(url)
  title = soup.title.string
  print(title)
   # 请求锁
  lock.acquire()
#   if title == "出错啦! - bilibili.com":
#      erroNum += 1
#   else:
#      erroNum = 0
  bilibili_url_search_DB.insert_total(url,title)
  # 释放锁
  lock.release() 
#   if erroNum > 1000:
#      break

print("开始爬取")
t1 = threading.Thread(target=printTitle,args=())
t2 = threading.Thread(target=printTitle,args=())
# t3 = threading.Thread(target=printTitle,args=())
# t4 = threading.Thread(target=printTitle,args=())
# t5 = threading.Thread(target=printTitle,args=())
# t6 = threading.Thread(target=printTitle,args=())
# t7 = threading.Thread(target=printTitle,args=())
# t8 = threading.Thread(target=printTitle,args=())
# t9 = threading.Thread(target=printTitle,args=())
# t10 = threading.Thread(target=printTitle,args=())

t1.start()
t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
# t7.start()
# t8.start()
# t9.start()
# t10.start()

t1.join()
t2.join()
# t3.join()
# t4.join()
# t5.join()
# t6.join()
# t7.join()
# t8.join()
# t9.join()
# t10.join()

print("爬完了！！！！！！！！！")