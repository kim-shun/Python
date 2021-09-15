#base

#import my_def
#from my_def import *
from my_def import f3bai,f3kaku
import sys
a = 555
b = 100
c = a + b


print("base_script")
#print(my_def.f2bai(3)) #6
print(f3bai(4)) #12
print(f3kaku(3,5)) #7.5
print(f3bai.__name__) #f3bai
print(f3bai.__doc__) #None → 関数の使い方
print(dir()) #ディレクトリ
#['__annotations__', '__builtins__', '__doc__',
#'__file__', '__loader__', '__name__', '__package__',
#'__spec__', 'a', 'b', 'c', 'f3bai', 'f3kaku', 'sys']
#メモリ上の名前を表示、この変数使ったかな
#print(my_def.f3kaku(20,12)) #120.0


print(sys.argv[0]) #/Users/kimurashunsuke/python/my_m/base.py
print(sys.argv[1])
print(sys.argv[2])

'''
ターミナルにて
kimurashunsuke@kimurashunsukenoMacBook-Air my_m % python3 base.py AAA bbb ccc
my_defの準備ができました
base_script
12
7.5
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'c', 'f3bai', 'f3kaku', 'sys']
base.py
AAA
bbb
'''
