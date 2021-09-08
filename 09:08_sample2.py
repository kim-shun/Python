def f(a,b,c):
    print(a + b + c)

f('test','だよ','ごめんね')

def f2(a, *b):
    print(a) #test
    print(b) #('A', 'B', 'C') 配列扱い?
    print(b[1]) #B

f2('test','A','B','C')
#*bの記述によって引数の数に食い違いがあってもエラーが起きない
