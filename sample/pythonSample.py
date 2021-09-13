a = 2
b = 3
c = a + b
print(c)
print(a + 5)
t = "TEXT"
tt = "text"
s = "aaaa\nbbbb\tccccdddd" #\nと\t
print(s,tt)
s2 = 'aaaabbbb"cccc\'\\dddd' #\の後の文字をそのまま表示させる
print(s2)

print("c:sample\\")
print(r"c:sample\\")
print('C:\some\name')
print(r'C:\some\name')
#rで\nをそのまま表示させる

'''
cccccccc
cccccccc
cccccccc
複数行のコメントアウト
'''

print(
    '''
cccc  cc
  cccc cc
cccc  cc
'''
    )
#\nを使わなくとも見た目のまま表示される

print(10/5)
#2ではなく2.0になる
print(3 * 'un' + 'ium')

print("""\
＝＝＝＝＝＝＝＝＝＝＝
Usage: thingy [OPTIONS]
 -h
 -H hostname
 ＝＝＝＝＝＝＝＝＝＝
"""
      )
#最初の\で改行をなくす


