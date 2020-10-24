[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/paigupai/ghost_soldier)

# ghost_soldier
Pythonを使ったWebスクレイピング
### acfun  
acfunの特定アニメのアクセス数を取得
https://www.acfun.cn/bangumi/aa6000218   
### levtech  
レバテック 各言語の求人数を取得して、sqlite内に保存する  
TODO: 保存したデータに築いて毎週、毎月の求人遷移画像を作成する。  その画像をWeChatにプッシュする。
### UR  
UR 各県の空き部屋のデータを取得  
使い方:
>安装python3  
>安装requests库  
>pip3 install requests  
>执行 UR_RealEstate.py 会生成对应的csv文件  
### dokodemo.world
dokodemo.world サイト内の各カテゴリーの商品名と画像を取得
使い方:
>安装requests库  
>更改config.py文件的目标值（TARGET）可以实现爬取不同分类的商品，总共13个分类Fashion
    ，Makeup
    ，Skincare
    ，Hair
    ，Bath_Body
    ，Health
    ，Kids_Family
    ，Sports_Outdoors
    ，Food_Drink
    ，Home
    ，Men
    ，Electronics
    ，Culture(Health之后的分类为TODO)  
>Target_Size为目标件数，可指定取得该分类商品的数目  
>优先爬取商品名和图片，图片会在当前程序所在文件夹下生成相应分类的文件夹，如果商品名中含有/字符，为了能生成文件/字符一概被删除。重名图片似乎会被直接覆盖  
>商品名和图片爬取完成后，会更新中文商品名，部分商品的中文商品名会缺失，原因调查中  
>启动方法为设定config之后，启动dokodemo_world.py
