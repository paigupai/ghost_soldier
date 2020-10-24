import sqlite3

total_sql = "insert into bilibili_url(url,title) values(?,?)"
# language_sql = "insert into market_facilitation_index(date,language,languageCount) values(?,?,?)"
# get_language_data_sql = "select * from market_facilitation_index where date > ? and date < ?;"

def create_db():
    print("create_db")
    con = sqlite3.connect('bilibili_url_search/bilibili_url.sqlite')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS bilibili_url(  ID INTEGER PRIMARY KEY   AUTOINCREMENT,"url" TEXT NOT NULL, "title" TEXT NOT NULL ) ;')
    con.close()

def insert_total(url,title):
    con = sqlite3.connect('bilibili_url_search/bilibili_url.sqlite')
    cur = con.cursor()
    cur.execute(total_sql, [url,title])
    con.commit()
    con.close()