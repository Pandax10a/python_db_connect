from sqlite3 import Cursor
import dbcreds
import mariadb

conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,
host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)

cursor = conn.cursor()

cursor.execute('CALL all_items')
result = cursor.fetchall()
print(result)