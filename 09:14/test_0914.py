print("\"Yes,\" they said")
#"Yes," they said
print(-5 ** 2 + 10) #-15
print((-5) ** 2 + 10) #35
'''
aa = 'hello'
aa

対話型'hello'

aa = 'hello',
aa
対話型('hello',)
'''

a = set('amehareyuki')
b = set('amedasu')
c = a - b
print(c)
#{'y', 'h', 'r', 'k', 'i'}
#{'r', 'i', 'y', 'h', 'k'} 順不動

#集合でないと引き算できない
#重複したものは消える

list1 = [40, 50, 60]
print(list1) #順序付きのデータ型
list1[0] = "a"
print(list1) #['a', 50, 60]

tuple1 = (50, "apple", 22.5) #順序付きで変更不可
#tuple1[1] = 2
#print(tuple1) #エラー

set1 = {'Germany','Japan', 'USA'} #順序なしで重複不可

dictionary1 = {'USA':1, 'Japan':2,'Germany':3}
