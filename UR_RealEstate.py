import requests
import json
import datetime
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
    'Postman-Token': "1a47a8db-cfb2-4a18-8c40-141c4bca9b7f,ed6f316a-c5ec-4066-94d5-c80c820766d7",
    'Host': "chintai.sumai.ur-net.go.jp",
    'Content-Length': "69",
    'cache-control': "no-cache"
    }
date = datetime.datetime.now()
title = date.strftime('%Y-%m-%d-%H-%M-%S')+"_東京.csv"
print(title)
file = open(f"{title}.csv",'w',encoding="utf-8")
#with open(title, "w",encoding="utf-8") as file:
file.write("物件名,地域,対象空室数,家賃(共益費),最寄駅,URL\n")
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
   station = date["access"].replace('<br>',' ')
   site_url = "https://www.ur-net.go.jp/%s"%(date["bukkenUrl"])
   money = (date["rent"]+date["commonfee"]).replace(',','')
   message ="%s,%s,%s,%s,%s,%s" %(date["name"],date["skcs"],date["roomCount"],money,station,site_url)
   print(message)
   file.write(message+"\n")
   print(date["name"])
  #print(date)
 #print(json_data)