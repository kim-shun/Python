print(list(map(lambda n: n * 3, [1,2,3]))) #[3, 6, 9]　無名関数

'''
def triple(n):
    return n * 3

print(list(map(triple,[1,2,3])))

    これをlambdaで1行に
'''

squares =[]
for x in range(10):
    squares.append(x**2)
print(squares) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



squares2 = list(map(lambda x: x**2, range(10)))
print(squares2) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares3 = [x**2 for x in range(10)]
print(squares3) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))
print(combs) #[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

from math import pi
print([str(round(pi,i)) for i in range(1,6)]) #['3.1', '3.14', '3.142', '3.1416', '3.14159']

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
m = [[row[i] for row in matrix] for i in range(4)]
print(m) #[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed) #[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

xy = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(xy) #[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]



