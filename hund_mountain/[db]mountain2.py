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

cursor.execute("DROP TABLE IF EXISTS mountain2")
cursor.execute('CREATE TABLE mountain2 (ID INT PRIMARY KEY, stnid TEXT, M_Time TEXT, M_level TEXT, M_reason TEXT, M_view TEXT, M_detail TEXT)')
# cursor.execute('alter table mountain1 add column HT int')
conn.commit()

# A열: id (산별기본키)
# B열: stnid (url요청할때id)
# C열: M_Time (소요시간)
# D열: M_level(난이도)
# E열: M_reason (선정이유)
# F열: M_view (개관)
# G열: M_detail (상세설명)


custom_header = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

# columns = [인덱스, url요청id , 소요시간, 난이도, 선정이유, 개관, M_상세설명]

data = pd.read_excel('source/mt_tl.xlsx')
data = data.where((pd.notnull(data)), '')
# print(data.head())

sql = 'insert into mountain2 (ID, stnid, M_Time, M_level, M_reason, M_view, M_detail) values(%s, %s, %s, %s, %s, %s, %s)'
for idx in range(len(data)):
    cursor.execute(sql, tuple(data.values[idx]))

conn.commit()