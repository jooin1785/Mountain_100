#Mountain1 table 생성

import MySQLdb
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

conn = MySQLdb.connect(
    user="root",
    password = os.environ.get("DB_PASSWORD"),
    host = "localhost",
    db = "hund_mountain",
    charset = 'utf8'
)
# print(type(conn))

cursor = conn.cursor()
print(type(cursor))

cursor.execute("DROP TABLE IF EXISTS mountain1") #기존의 mountain1테이블 삭제
cursor.execute('CREATE TABLE mountain1 (ID INT PRIMARY KEY, NAME TEXT, address_code INT, LAT FLOAT, LOT FLOAT, address TEXT, HT FLOAT, DESCRIPTION TEXT)')
# cursor.execute('alter table mountain1 add column HT int')
conn.commit()

custom_header = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

# columns = [인덱스, 산 이름, 산코드, 위도, 경도, 주소, 높이, 상세설명]

data = pd.read_excel('source/mt_100.xlsx')
# print(data.head())

sql = 'insert into mountain1 (ID, NAME, address_code, LAT, LOT, address, HT, DESCRIPTION) values(%s, %s, %s, %s, %s, %s, %s, %s)'
for idx in range(len(data)):
    cursor.execute(sql, tuple(data.values[idx]))

conn.commit()