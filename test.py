# from datetime import datetime

# date = datetime.strptime('2018-09-11 12:45:00', '%Y-%m-%d %H:%M:%S')
# print(date)

import psycopg2


conn = psycopg2.connect(
    host='ziggy.db.elephantsql.com',
    user='jlhnbbhm',
    database='jlhnbbhm',
    password='ZNt-0Xz6h2zq_GWs6YbzCjAlgtKbryQh'
)

cur = conn.cursor()
cur.execute('select * from lectores')
print(cur.fetchall())

cur.close()
conn.close()
