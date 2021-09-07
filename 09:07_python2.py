'''
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


print(8//2) #4
print(8/2) #4.0

for n in range(2, 10):
    print(n, "学年")
    for x in range(2, n):
        print(x,"組")

for n in range(2, 10):
    print(n)
    for x in range(2,n):
        print(x)
        if x == 4:
            #break #5以上でも4でbreak 親のforに抜ける
            #continue


print(2%2) #0
print(2//2) #1


for i in range(2,2):
    print(i) #何も表示されない


for n in range(2,10):
    print(n)
else:


'''

for n in range(2, 10):
    print(n) # 2 3 4
    if n == 4:
        #print(n) #4
        break
    #print(n) #2 3
else:
    print("for_end")

fruits = ["apple","banana","cherry","durian"]
for item in fruits:
    print(item)



            
        
