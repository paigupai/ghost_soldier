import requests
import urllib.parse
import json
import database
import sys
import config
import os

# with open(os.path.join('/path/to/Documents',completeName), "w") as file1:
#     toFile = raw_input("Write what you want into the field")
#     file1.write(toFile)
def download_img(url, file_name):
    print("开始取得图片:%s"%file_name)
    path = "dokodemo_world/" + config.Folder_Name +"/"
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = file_name + ".png"
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(os.path.join(path, file_name), 'wb') as f:
            f.write(r.content)
    else:
        print("图片取得失败")

def get_chinese_name():
    print("开始取得商品中文名")
    url = "https://wwqqkderx1.execute-api.ap-northeast-1.amazonaws.com/search/front/search/first"

    payload = "{\"page\":1,\"sort\":1,\"size\":" + str(config.Target_Size) + ",\"keyword\":\"\",\"category_id\":\"" + config.Category_Id + "\",\"maker_id\":null,\"brand_id\":null,\"shop_id\":null,\"refine\":{\"price_low\":null,\"price_high\":null,\"made_in_jp\":null,\"set_sales\":null,\"maker_id\":null,\"brand_id\":null,\"color\":null,\"clothing_size\":null,\"shoe_size\":null,\"child_clothing_size\":null,\"child_shoe_size\":null,\"dia\":null,\"diopter\":null,\"medicine\":null,\"exhibit\":true}}"
    headers = {
    'authority': 'wwqqkderx1.execute-api.ap-northeast-1.amazonaws.com',
    'x-dkdm-scd': '840',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'content-type': 'application/json',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-dest': 'empty',
    'x-dkdm-ccd': 'USD',
    'x-dkdm-cid': '-1',
    'x-dkdm-gid': '2',
    'origin': 'https://dokodemo.world',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'referer': 'https://dokodemo.world/zh-Hans/es/category/1712/',
    'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    json_data = response.json()
    json_dict = json.loads(json_data) 

    product_data_list = json_dict['product']
    if not product_data_list:
        print("中文商品已全部取得")
        return
    for product_data in product_data_list:
        product_id = product_data['product_id']
        product_name = product_data['product_name'].replace("%20", " ")
        print(product_id)    
        #URLデコード
        chinese_product_name = urllib.parse.unquote(product_name)
        print(chinese_product_name)
        #去掉/ 命名统一
        chinese_product_name = chinese_product_name.replace('/', '')
        database.update_chinese_name(product_id,chinese_product_name)
    print("商品中文名取得完成")


database.create_db()
#目标
#target = config.Target.Makeup
config.setup()
print("目标为%s"%config.Folder_Name)

url = "https://wwqqkderx1.execute-api.ap-northeast-1.amazonaws.com/search/front/search/first"

payload = "{\"page\":1,\"sort\":1,\"size\":" + str(config.Target_Size) + ",\"keyword\":\"\",\"category_id\":\"" + config.Category_Id + "\",\"maker_id\":null,\"brand_id\":null,\"shop_id\":null,\"refine\":{\"price_low\":null,\"price_high\":null,\"made_in_jp\":null,\"set_sales\":null,\"maker_id\":null,\"brand_id\":null,\"color\":null,\"clothing_size\":null,\"shoe_size\":null,\"child_clothing_size\":null,\"child_shoe_size\":null,\"dia\":null,\"diopter\":null,\"medicine\":null,\"exhibit\":true}}"
headers = {
  'authority': 'wwqqkderx1.execute-api.ap-northeast-1.amazonaws.com',
  'x-dkdm-scd': '840',
  'origin': 'https://dokodemo.world',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
  'content-type': 'application/json',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'sec-fetch-dest': 'empty',
  'x-dkdm-ccd': 'USD',
  'x-dkdm-cid': '-1',
  'x-dkdm-gid': '1',
  'sec-fetch-site': 'cross-site',
  'sec-fetch-mode': 'cors',
  #TODO 这里没用到？？1712
  'referer': 'https://dokodemo.world/ja/es/category/1712/',
  'accept-language': 'ja,en-US;q=0.9,en;q=0.8'
}

response = requests.request("POST", url, headers=headers, data = payload)
#json data
json_data = response.json()
json_dict = json.loads(json_data) 

product_data_list = json_dict['product']
if not product_data_list:
 print("商品已全部取得")
 get_chinese_name()
 sys.exit() 
i = 1
for product_data in product_data_list:
    product_id = product_data['product_id']
    product_name = product_data['product_name'].replace("%20", " ")
    image_path = "https://d89ge5hfdpmo8.cloudfront.net/mall/" + product_data['image_path']

    print(product_id)    
    #URLデコード
    japanese_product_name = urllib.parse.unquote(product_name)
    print(japanese_product_name)
    print("目前件数：" + str(i))
    #data clear
    #去掉/ 不然会无法创建文件
    japanese_product_name = japanese_product_name.replace('/', '')
    #保存至DB
    database.insert_db(product_id,japanese_product_name)
    #取得图片
    download_img(image_path,japanese_product_name)
    i = i + 1
get_chinese_name()



# def download_img(url, file_name):
#     print("开始取得图片:%s"%file_name)
#     file_name ="dokodemo_world/" + config.Folder_Name +"/"+ file_name
#     r = requests.get(url, stream=True)
#     if r.status_code == 200:
#         with open(file_name, 'wb') as f:
#             f.write(r.content)
#     else:
#         print("图片取得失败")