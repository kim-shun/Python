import mysql.connector

config = {
    'user':'root',
    'port':'3306',
    'password':'',
    'host':'localhost'
    'database':'my_python'
    }
dbconnector = mysql.connector.connect(**config)

if dbconnector.is_connected():
    print('接続成功')
else:
    print('接続失敗')
    exit(1)

cursor = dbconnector.cursor(buffered=True)
