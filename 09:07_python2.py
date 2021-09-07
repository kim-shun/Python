for i in range(5):
    if i == 2:
        #print("True")
        #break(それ以降)
        continue #出てきた時点で下のコードをスルーする(その周)
        #print("True") #2が消える
    else:
        print(i)

print()

for n in range(2,10):
    for x in range(2, n):

        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
