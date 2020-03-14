import sqlite3


con = sqlite3.connect('dokodemo_world/dokodemo.sqlite')
cur = con.cursor()

def create_db():
    cur.execute('CREATE TABLE IF NOT EXISTS product( "product_id" TEXT NOT NULL, "product_name" TEXT NOT NULL, "chinese_name" TEXT, PRIMARY KEY("product_id") ) ;')
    print("DB作成成功")


def insert_db(id,name):
    insert_sql = "insert into product(product_id,product_name) values(?,?);"
    print("保存产品:%s"%name)
    cur.execute(insert_sql, [id,name])
    con.commit()
    print("保存成功")


def update_chinese_name(id,name):
    update_chinese_name_sql = "update product set chinese_name = ? where product_id = ?;"
    print("更新产品中文名:%s"%name)
    cur.execute(update_chinese_name_sql, [name,id])
    con.commit()
    print("保存成功")