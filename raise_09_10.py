class MyEx(Exception):
    pass

def f(a,b):
    try:
        if b < 0 or a < 0:
            raise MyEx("マイナスはだめです")
        
        print(a / b)
    except ZeroDivisionError:
        print("0で割ったらいけません")
    except MyEx as e:
        print(e)
    finally:
        print("END")

f(10,5)
f(10,0)
f(10,-2) #強制的にエラーにする
f(-50,9)

#Exception エラーを処理する大親分

#親子の継承
#CもDもBと同じこともできる

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

#cls()をBCDに入れたから書かなくて良い
for cls in [B,C,D]:
    #print(cls) #<class '__main__.B'> <class '__main__.C'> <class '__main__.D'>
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

#B
#C
#D
        '''
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")

    の場合
    B
    B
    B
    になる
    親子関係の問題
    全員大親分をExceptionにしたらBBBでなくなる
    '''









