import MySQLdb
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


# 지하철역, 기차역, 고속버스터미널 DB저장

conn = MySQLdb.connect(
    user="root",
    password = os.environ.get("DB_PASSWORD"),
    host = "localhost",
    db = "hund_mountain",
    charset = 'utf8'
)


cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS subway")
cursor.execute('CREATE TABLE subway (id INT PRIMARY KEY, st_name TEXT, lot FLOAT, lat FLOAT)')
conn.commit()

custom_header = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

data = pd.read_excel('source/subway_station.xlsx')

sql = 'insert into subway (id, st_name, lot, lat) values(%s, %s, %s, %s)'
for idx in range(len(data)):
    cursor.execute(sql, tuple(data.values[idx]))

conn.commit()




cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS train")
cursor.execute('CREATE TABLE train (id INT PRIMARY KEY, st_name TEXT, addr TEXT, lat FLOAT, lot FLOAT)')
conn.commit()

custom_header = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

data = pd.read_excel('source/train_station.xlsx')

sql = 'insert into train (id, st_name, addr, lat, lot) values(%s, %s, %s, %s, %s)'
for idx in range(len(data)):
    cursor.execute(sql, tuple(data.values[idx]))
conn.commit()




cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS bus")
cursor.execute('CREATE TABLE bus (id INT PRIMARY KEY, st_name TEXT, addr TEXT, lat FLOAT, lot FLOAT)')
conn.commit()

custom_header = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

data = pd.read_excel('source/bus_station.xlsx')

sql = 'insert into bus (id, st_name, addr, lat, lot) values(%s, %s, %s, %s, %s)'
for idx in range(len(data)):
    cursor.execute(sql, tuple(data.values[idx]))
conn.commit()

