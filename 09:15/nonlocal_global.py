#変数のスコープ
'''
print('変数のスコープ')
msg = 'hello グローバル' #グローバル(プログラムの本線)変数
def greet():
    global msg #グローバル扱いにされる
    msg  = 'hi ローカル' #ローカル変数(関数の中)
    print(msg)

greet() #hi
print(msg) #hello

#同じ名前の変数は同じ変数にしたい→global

#global msg
#hi ローカル
#hi ローカル
'''
#n = 0
def count():
    n = 0
    n += 1
    return n

print(count()) #1
print(count()) #1
print(count()) #1
#毎度nが初期化される

n = 0
def count2():
    global n
    n += 1
    return n

print(count2()) #1
print(count2()) #2
print(count2()) #3


def f_out():
    n = 0
    def count3():
        nonlocal n
        n += 1
        return n
    return count3
counter = f_out()

print(counter()) #1
print(counter()) #2
print(counter()) #3




