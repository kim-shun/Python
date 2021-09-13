#inputはString型
zz = int(input("数字は？"))
x = 0
y = 0
#z = 20
while x < zz:
    print(x)
    x += 1
    y += x
    print('Y=',y)
print(y) #zz = 10の時55
print("END")

print()

a, b = 0,1
while a < 10:
 #   print(a)
    a,b = b, a+b
    print(a, end= ",") #1,1,2,3,5,8,13,END

print("END")
#半角4つかないと正しく読み込まれない
#フィボナッチ数列
