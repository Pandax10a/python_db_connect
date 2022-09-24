
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
    while True:
        try:
            the_num = int(input('what price you want? '))
            only_one(the_num)
            return the_num
        except ValueError:
            print('use only number')

def only_one(num):
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,
    host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)

    cursor = conn.cursor()
    while True:
        try:
            cursor.execute('CALL price_greater_than(?)', [num])
            break
        except mariadb.OperationalError:
            print('use an integer')
            
        
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    print(result)

# user_price(result)

user_price()
    