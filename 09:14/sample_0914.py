print('{0} and {1}'.format('spam','egg'))
#spam and egg
#f = open('workfile', 'w')
#ファイルの読み込みと書き込み(read,write)
#'r+'は読み書き両方、追加は'a'
'''
with open('workfile') as f:
    read_data = f.read()

#We can check that the file has been automatically closed
f.closed
'''
#openのままにしない
#withやf.close()を使わずに呼び出すとf.write()の実引数がディスクに正常に書き込まれないことがある
