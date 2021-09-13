def fib2(n):
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b = b, a + b
    return result
obj = fib2(50)
print(obj)

def fib(n):
    a,b = 0,1
    while a < n:
        print(a, end=' ')
        a,b = b, a+b
fib(150)

print()

for i in range(1,3):
    for j in range(1,6):
        print(j,end= ",")
        if i * j > 3:
            break
print()

for i in range(3):
    for j in range(4):
        if j % 2 == 1:
            print(j,end=',')
            #break
print()

for n in range(2, -15, -3):
    if n % 2 == 0:
        print(n, end= ",")
        continue
