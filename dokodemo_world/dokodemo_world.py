import requests
import urllib.parse
import json

url = "https://wwqqkderx1.execute-api.ap-northeast-1.amazonaws.com/search/front/search/first"

payload = "{\"page\":2,\"sort\":1,\"size\":45,\"keyword\":\"\",\"category_id\":\"1712\",\"maker_id\":null,\"brand_id\":null,\"shop_id\":null,\"refine\":{\"price_low\":null,\"price_high\":null,\"made_in_jp\":null,\"set_sales\":null,\"maker_id\":null,\"brand_id\":null,\"color\":null,\"clothing_size\":null,\"shoe_size\":null,\"child_clothing_size\":null,\"child_shoe_size\":null,\"dia\":null,\"diopter\":null,\"medicine\":null,\"exhibit\":true}}"
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
  'referer': 'https://dokodemo.world/ja/es/category/1712/',
  'accept-language': 'ja,en-US;q=0.9,en;q=0.8'
}

response = requests.request("POST", url, headers=headers, data = payload)
#json data
json_data = response.json()
json_dict = json.loads(json_data) 

product_data_list = json_dict['product']
for product_data in product_data_list:
    product_name = product_data['product_name'].replace("%20", " ")
    #URLデコード
    print(urllib.parse.unquote(product_name))