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

cursor = conn.cursor()
print(type(cursor))
cursor.execute("DROP TABLE IF EXISTS mountain3")

cursor.execute('CREATE TABLE mountain3 (id INT PRIMARY KEY, areatreason TEXT, areanm TEXT, details TEXT, etccourse TEXT, mntheight FLOAT, mntnm TEXT, overview TEXT, subnm TEXT, tourisminf TEXT, transport TEXT)')
conn.commit()


custom_header = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

data = pd.read_excel('source/mt_100_3.xlsx')
data = data.where((pd.notnull(data)), '')

sql = 'insert into mountain3 (id, areatreason, areanm, details, etccourse, mntheight, mntnm, overview, subnm, tourisminf, transport) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
for idx in range(len(data)):
    cursor.execute(sql, tuple(data.values[idx]))

conn.commit()

