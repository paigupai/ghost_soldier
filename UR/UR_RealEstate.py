import requests
import json
from datetime import datetime, timedelta, timezone
from bs4 import BeautifulSoup
#东京地区
tokyo_area_list = ["01","02","03","04","05","06"]

url = "https://chintai.sumai.ur-net.go.jp/chintai/api/bukken/search/list_bukken/"

headers = {
    'Connection': "keep-alive",
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'Origin': "https://www.ur-net.go.jp",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
    'Sec-Fetch-Site': "same-site",
    'Sec-Fetch-Mode': "cors",
    'Referer': "https://www.ur-net.go.jp/chintai/kanto/tokyo/list/",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "ja,en-US;q=0.9,en;q=0.8",
    'Cache-Control': "no-cache",
    'Host': "chintai.sumai.ur-net.go.jp",
    'Content-Length': "69",
    'cache-control': "no-cache"
    }
# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), 'JST')
# GOOD, タイムゾーンを指定している
date = datetime.now(JST)
title = date.strftime('%Y-%m-%d-%H-%M-%S')+"_東京"
print(title)
file = open(f"{title}.csv",'w',encoding="utf-8")
#with open(title, "w",encoding="utf-8") as file:
file.write("物件名,地域,対象空室数,家賃(共益費),間取り/床面積,最寄駅,URL\n")
for area in tokyo_area_list:
 print(area)
 payload = "rent_low=&rent_high=&floorspace_low=&floorspace_high=&tdfk=13&area=%s"%(area)
 response = requests.request("POST", url, data=payload, headers=headers)
 #json化
 json_array = json.loads(response.text,encoding='utf-8')
 # 新建文件保存内容
 ur_net = "https://www.ur-net.go.jp/"
 for date in json_array:
  if date["roomCount"] > 0:
   #清洗数据
   station = date["access"].replace('<br>','/')
   site_url = "https://www.ur-net.go.jp/%s"%(date["bukkenUrl"])
   money = (date["rent"]+date["commonfee"]).replace(',','')
   #layout
   layout = get_layout(site_url)
   message ="%s,%s,%s,%s,%s,%s,%s" %(date["name"],date["skcs"],date["roomCount"],money,layout,station,site_url)
   print(message)
   file.write(message+"\n")
   #print(date["name"])
  #print(date)
 #print(json_data)


 def get_layout(url):
     headers = {
     'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
     'Accept': "*/*",
     'Cache-Control': "no-cache",
     'Host': "www.ur-net.go.jp",
     'Accept-Encoding': "gzip, deflate",
     'Connection': "keep-alive",
     'cache-control': "no-cache"
     }
     response = requests.request("GET", url, headers=headers)
     # 将网页编码方式转换为utf-8
     response.encoding = 'utf-8'
     # 网站源码
     html = response.text
     # lxml化
     soup = BeautifulSoup(html,'lxml')
     # 間取り/床面積
     layout_data = soup.find('div',class_='article_sliders_table').find_all('td')
     layout = layout_data[1].find('p').string
     #print(layout)
     return layout