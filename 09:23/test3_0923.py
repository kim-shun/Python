x = ["a","b","c","d","e"]
print(x[:-3])
#['a', 'b']

from math import pi
print(pi) #3.141592653589793
print(round(pi,1)) #3.1
print(round(pi,4)) #3.1416
m = [str(round(pi, i)) for i in range(0, 5)]
print(m)
#['3.0', '3.1', '3.14', '3.142', '3.1416']

#クリーンアップ動作を定義してあるオブジェクトに対して、クリーナップ動作を保証した形で利用するための構文　with

#最初にtry節が実行される。
#try節の実行中に例外が発生すると、try節中の残りはスキップされる。
#例外の型がexcept節にある名前と一致しない場合、送出された例外はさらに外側にあるtry文に渡される。
'''
直接実行されるPythonプログラムコードのことを指して特に、
Pythonスクリプトと呼びます。
モジュールかスクリプトかを区別しないときには、
Pythonソースファイルや .py ファイル等と呼ばれます。
'''