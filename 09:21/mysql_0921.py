'''
# db_201 MySQL サーバへ接続
import mysql.connector
# コネクションの作成
config = {
    'user':'root',
    'password':'',
    'host':'localhost' }

# try except
try:
    dbconnector = mysql.connector.connect(**config) # 例外メッセージ
except mysql.connector.Error as errmsg:
    print('接続失敗しました。')
    print('メッセージ:',errmsg)
# 成功した場合、接続を切断
else:
    print('接続成功しました!')
    print('即切断します')
    dbconnector.close()

print('END')
'''

# db_202 MySQL サーバへ接続
import mysql.connector
# コネクションの作成
config = {
    'user':'root',
    'password':'',
    'host':'localhost'
    }
# try except
try:
    dbconnector = mysql.connector.connect(**config) # 例外メッセージ
except mysql.connector.Error as errmsg:
    print('接続失敗しました。')
    print('メッセージ:',errmsg)
    # exit(1)
# cursorオブジェクトの生成
cursor = dbconnector.cursor()
# SQL命令を実行
cursor.execute("DROP DATABASE IF EXISTS y_sampledb")
cursor.execute("CREATE DATABASE y_sampledb")
cursor.execute("SHOW databases")
# 実行結果データを取得、表示
tuples = cursor.fetchall()
for tpl in tuples:
    print(tpl[0])
# コミットする(実際に保存する)
dbconnector.commit()
# 切断
dbconnector.close()
print('END')
