
import dbcreds
import mariadb


conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,
host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)

cursor = conn.cursor()

cursor.execute('CALL all_items')
result = cursor.fetchall()


cursor.close()
conn.close()

for each in result:
    print(each)

def user_price():
    the_num = input('what price you want? ')
    only_one(the_num)
    return the_num

def only_one(num):
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,
    host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)

    cursor = conn.cursor()
    
    cursor.execute('CALL price_greater_than(?)', [num])
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    print(result)

# user_price(result)

user_price()
    