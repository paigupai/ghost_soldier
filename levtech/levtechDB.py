import sqlite3

con = sqlite3.connect('levtech/levtech.sqlite')
cur = con.cursor()
total_sql = "insert into search_count(date,total) values(?,?)"
language_sql = "insert into market_facilitation_index(date,language,languageCount) values(?,?,?)"
get_language_data_sql = "select * from market_facilitation_index where date > ? and date = ?;"

def create_db():
    cur.execute('CREATE TABLE IF NOT EXISTS search_count( "date" dateTIME NOT NULL, "total" INTEGER NOT NULL, PRIMARY KEY("date") ) ;')
    cur.execute('CREATE TABLE IF NOT EXISTS market_facilitation_index( "date" dateTIME NOT NULL, "language" TEXT NOT NULL, "languageCount" INTEGER, PRIMARY KEY("date","language") ) ;')


def insert_total(date,total):
    cur.execute(total_sql, [date,total])
    con.commit()


def insert_language(date,language,languageCount):
    cur.execute(language_sql, [date,language,languageCount])
    con.commit()

def get_language_data(startDate,endDate):
    cur.execute(get_language_data_sql, [startDate,endDate])
    return cur.fetchall()