def f(a):
    try:
        #メインの処理をここに書かないといけない
        x = 10 / a
        print(x)
        print(v) #NameError
    except ZeroDivisionError:
        print("ゼロで割ったらいけません")
    except TypeError:
        print("文字ではなく数字を入力してください")
    except NameError:
        print("その変数は定義されていません")
    #else:
        #print("それ以外の処理")
    #finally:
        #print("最後にしたい処理")
        
print("END")

f(4) #2.5
f(0) #ZeroDivisionError: division by zero → ゼロで割ったらいけません
f(2) #5.0
f(0.4) #25.0
f("t") #TypeError: unsupported operand type(s) for /: 'int' and 'str' → 文字ではなく数字を入力してください
f(abc) #NameError: name 'abc' is not defined　この行でエラーが起きているため、処理できない
f(150)
