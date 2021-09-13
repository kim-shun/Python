squares = []
for x in range(10):
    squares.append(x**2)

print(squares) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


#map

def triple(n):
    return n * 3

print(list(map(triple,[1,2,3]))) #[3, 6, 9]



s = list(range(5))
print(s) #[0, 1, 2, 3, 4]

def mk(x):
    y = x * 2
    return y

m = map(mk,s)
print(m) #<map object at 0x7ff225bcf190> オブジェクトそのものの名前
print(list(m)) #[0, 2, 4, 6, 8]

print(mk(3)) #6
print(mk([1,2,3])) #[1, 2, 3, 1, 2, 3]

