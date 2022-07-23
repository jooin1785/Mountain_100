# 산악기상정보시스템에서 실시간 데이터 크롤링 및 db 자동저장(불쾌지수 포함)

import MySQLdb
import requests
import json
import os
from dotenv import load_dotenv


name = []
day = []
rainp = []
temp = []
hum = []
wspd = []
num = []
di = []
custom_header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
for i in range(1, 101):
    url = f'http://mtweather.nifos.go.kr/famous/mountainOne?stnId={i}'
    try:
        req = requests.get(url, headers = custom_header).text
        document = json.loads(req)
    except:
        continue
    try:
        others = document['others']
        weather_info = document['hr3List']
    except KeyError:
        continue
    for ls in range(len(weather_info)):
        num.append(i)
        day.append(weather_info[ls]['tmEf'])
        rainp.append(weather_info[ls]['rainp'])
        temp.append(weather_info[ls]['temp'])
        hum.append(weather_info[ls]['humi'])
        wspd.append(weather_info[ls]['wspd'])
        name.append(document['famousMTSDTO']['stnName'])
        tp = weather_info[ls]['temp']
        hm = weather_info[ls]['humi']
        D_I = (1.8 * tp) - (0.55 * (1 - hm/100) * ((1.8 * tp) - 26)) + 32
        #print(D_I)
        di.append(D_I)

print(num)


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
cursor.execute("DROP TABLE IF EXISTS live_weather")
cursor.execute('CREATE TABLE live_weather (ID INT PRIMARY KEY,num INT , name TEXT, day INT, rainp INT, temp FLOAT, hum INT, wspd FLOAT, di FLOAT)')
# columns = ['id', '이름', '시간', '강수 확률', '기온', '습도', '풍속', '불쾌지수']

sql = 'insert into live_weather (ID, num, name, day, rainp, temp, hum, wspd, di) values(%s,%s, %s, %s, %s, %s, %s, %s, %s)'
l=len(hum)
for i in range(l):
    cursor.execute(sql,(i, num[i],name[i],day[i],rainp[i],temp[i],hum[i],wspd[i],di[i]))

conn.commit()