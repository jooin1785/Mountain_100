#지역에 따른 위도,경도 포함된 coordinate 테이블 생성

import MySQLdb
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv()

conn = MySQLdb.connect(
    user="root",
    password=os.environ.get("DB_PASSWORD"),
    host = "localhost",
    db = "hund_mountain",
    charset = 'utf8'
)
# print(type(conn))

cursor = conn.cursor()
print(type(cursor))
# columns = [areaCode,시도,위도,경도]
cursor.execute('CREATE TABLE coordinate (areaCode INT PRIMARY KEY, area TEXT, lat FLOAT, lot FLOAT)')
# cursor.execute('alter table mountain1 add column HT int')
conn.commit()

custom_header = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}



data = pd.read_excel('source/coordinate.xlsx')
# print(data.head())

sql = 'insert into coordinate (areaCode, area, lat, lot) values(%s, %s, %s, %s)'
for idx in range(len(data)):
    cursor.execute(sql, tuple(data.values[idx]))

conn.commit()