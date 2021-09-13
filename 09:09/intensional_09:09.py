'''
vec = [-4, -2, 0, 2, 4]
vv = [x * 2 for x in vec]
print(vv) #[-8, -4, 0, 4, 8]
vvv = [x for x in vec if x > 0]
print(vvv) #[2, 4]
vvvv = [abs(x) for x in vec]
print(vvvv) #[4, 2, 0, 2, 4]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  '] #スペースつきの文字列
ff = [weapon.strip() for weapon in freshfruit]
print(freshfruit) #['  banana', '  loganberry ', 'passion fruit  ']
print(ff) #['banana', 'loganberry', 'passion fruit']

tt = [(x, x**2) for x in range(6)]
print(tt) #[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

#forを使ってリストを平滑化(1次元化)する
vec2 = [[1,2,3],[4,5,6],[7,8,9]]
ve = [num for elem in vec2 for num in elem]
print(ve) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#関数呼び出しのネスト

#simport * #色々import
from math import pi #mathモジュールのπ
print(pi) #3.141592653589793
p = [str(round(pi,i)) for i in range(1,6)] #str出なくても良い
print(p) #['3.1', '3.14', '3.142', '3.1416', '3.14159']

n = 4.555667778889999
print(round(n,4)) #4.5557 小数点4桁まで、末尾は四捨五入された値

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
print(matrix) #[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print([[row[i] for row in matrix] for i in range(4)])
#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
'''

m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(m[1]) #[5, 6, 7, 8]
print(m[2][0]) #9
t = []
for i in range(4):
    t.append([row[i] for row in m])
    print(t)
    #[[1, 5, 9]] (m[0][0],m[1][0],m[2][0])
    #[[1, 5, 9], [2, 6, 10]]
    #[[1, 5, 9], [2, 6, 10], [3, 7, 11]]
    #[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print(t) #[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

t2 = []
for i in range(3):
    t2.append([row[2] for row in m])
    print(t2)
    #[[3, 7, 11]]
    #[[3, 7, 11], [3, 7, 11]]
    #[[3, 7, 11], [3, 7, 11], [3, 7, 11]]
print(t2) #[[3, 7, 11], [3, 7, 11], [3, 7, 11]]

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

print(list(zip(*matrix)))
#[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

names = ["Alice","Bob","Kevin"]
ages = [18,23,30]

for name,age in zip(names,ages):
    print(name,age)
'''
Alice 18
Bob 23
Kevin 30
'''
