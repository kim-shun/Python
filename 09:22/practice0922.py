a = ['a','b','c']
for k,v in enumerate(a):
    print(k,v)

print()

for i in [0,1,2]:
    print(i,a[i])
print()

'''
0 a
1 b
2 c
'''

vec = [[1,2,3],[4,5,6],[7,8,9]]
print([num for elem in vec for num in elem])
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

print()

i = 0
while i < 5:
    print(i,end=",")
    i += 1
else:
    print("END", end=",")
print("END")
#0,1,2,3,4,END,END

print()

for i in range(7):
    if i == 5:
        break
    print(i,end=",")
else:
    print("END")
#0,1,2,3,4,
print()

#print(list(filter(lambda n:n % 3 == 0, range(10))))
#[0, 3, 6, 9]
#filterなしだとTypeError: list expected at most 1 argument, got 2

data = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
result = list(zip(*data))
print(result)
#[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
print()

a,b = 0,1
while b < 10:
    print(b,end=",")
    a,b = b, a+b
#1,1,2,3,5,8,

print()
a,b = 0,1
while b < 10:
    print(a,end=",")
    a,b = b, a+b
#0,1,1,2,3,5,
print()

for i in range(6):
    if i == 3:
        continue
    print(i,end=",")
else:
    print("END")
#0,1,2,4,5,END
