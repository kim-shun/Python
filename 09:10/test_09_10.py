'''
a,b,c = 0,5,8
if a:
    print(True)
else:
    print(False)

'''

#よく分からない
def f(a, *b):
    print("a=",a)
    print("b=",b)
    for i in b:
        print(i,end='')
f('H1','H2','H3','H4')

print()

#よく分からない
for i in range(1,3):
    print("i学年=",i)
    for j in range(1,4):
        print("jクラス=",j)
        s = i * j
        print(s,end=",")
        print()


