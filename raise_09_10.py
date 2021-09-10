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
