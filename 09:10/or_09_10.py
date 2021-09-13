'''
str1,str2,str3 = '','Trondheim','Hammer Dance'
non_null = str1 or str2 or str3
print(non_null) #Trondheim
non_null2 = str1 and str2 and str3
print(non_null2) #空っぽ

print(str1 or str3 or str2) #Hammer Dance

#orは1個目がTrueだったら2個目はみない(評価しない)
#notが優先順位高い


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f) #apple banana orange pear #abc順になる

#setにする = 集合にする(重複がなくなる)
print(basket) #['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
#中身が変更されているわけではない

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data) #[56.2, 51.7, 55.3, 52.5, 47.8]
print(raw_data) #[56.2, nan, 51.7, 55.3, 52.5, nan, 47.8]


for i in reversed(range(1,10,2)):
    print(i) #9 7 5 3 1
'''
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)
#gallahad the pure キーとバリュー
#obin the brave キーとバリュー



for i,v in enumerate(['tic','tac','toe']):
    print(i,v)
#0 tic
#1 tac
#2 toe

for i in enumerate(['tic','tac','toe']):
    print(i)

#(0, 'tic')
#(1, 'tac')
#(2, 'toe')


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q,a in zip(questions,answers):
    print('What is your {0}? It is {1}.'.format(q,a))


#What is your name? It is lancelot.
#What is your quest? It is the holy grail.
#What is your favorite color? It is blue.

a = set('abracadabra')
print(a) #{'b', 'c', 'd', 'a', 'r'} #重複なしでバラバラ

t = 12345, 54321, 'hello'
print(t) #(12345, 54321, 'hello')
x,y,z = t
print(x) #12345
print(y) #54321

