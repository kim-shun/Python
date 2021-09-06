'''
a = 'hello'
b = 'tom'
c = a + b
print(c)
age = 23
print(c, age)
print('私は', b, 'です')
print('名前は: %s, 年齢は: %d' % (b,age))
print("名前は {0}, 年齢は {1}".format(b,age))


a = [20,30,40]
b = 5
print(a)
print(a[0])
print(a[1])

a[1] = b
print(a)

a = {"x":45,"y":300,"w":20}
b = 5
print(a)

for i in a:
    print(a[i]) #45 300 20

a["y"] = b
print(a)

for i in a:
    print(a[i])

print("END")



i = 0
for num in range(11):
    print(num)
    i += num
print("合計", i)



a = int(input("数値を入力してください"))
i = 0
num = 0
a += 1
for num in range(a):
    print(num)
    i += num
print("1から", a - 1, "までの合計は",i, "です")

'''

a = int(input("数値を入力してください"))
num = 1
a += 1
i = 0
print("Start")
while num < a:
    i += num
    print("足し算", num)
    num += 1

print("合計", i)
