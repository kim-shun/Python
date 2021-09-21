# db_202 MySQL サーバへ接続
import mysql.connector
# コネクションの作成
config = {
    'user':'root',
    'port':'3306',
    'password':'',
    'host':'localhost',
    'database':'my_python'
    }
dbconnector = mysql.connector.connect(**config) # 接続できるか確認
if dbconnector.is_connected():
    print('接続成功')
else:
    print('接続失敗')
    Db_203.py
    exit(1)
'''
# cursorオブジェクトの生成
cursor = dbconnector.cursor(buffered=True)
# id,name,gender,age
# SQL命令を実行
cursor.execute("DROP TABLE IF EXISTS memberlist;")
cursor.execute("CREATE TABLE memberlist ( mid INT, name CHAR(20), gender CHAR(10), age INT, PRIMARY KEY (mid) );")
cursor.execute("INSERT INTO memberlist VALUES ( 1, 'h_tanaka','W',28);")
cursor.execute("INSERT INTO memberlist VALUES ( 2, 's_yamada','M',32);")
cursor.execute("INSERT INTO memberlist VALUES ( 3, 'm_sato','W',21);")
cursor.execute("INSERT INTO memberlist VALUES ( 4, 'h_abe','M',25);")
# コミットする(実際に保存する)
dbconnector.commit()
# 問い合わせ
cursor.execute("SELECT * FROM memberlist;")
# 全てのデータを取得、表示
tuples = cursor.fetchall()
print("テーブル memberlist のデータ:")
for tpl in tuples:
    print(tpl) # 切断
'''
dbconnector.close()
print('END’)
