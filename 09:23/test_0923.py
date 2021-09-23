#関数.clear() == del 関数[:]
#コマンドライン引数を取得するためのモジュール sys
#ブール演算子and及びorは短絡演算子という。
#【誤】比較はブール演算のand及びorによって組み合わせることができ、また比較の結論はnotにより否定ができる。これらの優先順位は比較演算子よりも高い。
#関数をコールするときは、必ず位置引数が先でキーワード引数を後にしなければならない。キーワード引数(city='Tokyo')
#仮想環境にインストールされたすべてのパッケージを表示するpipのオプション：pip list
#タプルは「immutable」であり、 アンパッキングしてアクセスすることができる。
#【誤】リストは「mutable」であり、 タプルの中に格納することができない
#ログを取得するためのモジュール：logging
#【誤】変数に値を代入しないで実行しようとするとTypeErrorが表示される　→NameError
#関数内で変数に代入を行うと、その値がローカル変数のシンボル表に記録される
#【誤】関数内からグローバル変数は参照することができない
#コンパイル済Pythonファイルの拡張子：pyc
#変数とモジュール名の補完はインタプリタの起動時に自動で有効になっており、[Tab]キーで補完機能が呼び出せる。

#print(num) #NameError: name 'num' is not defined
#print('100' + 2) #TypeError: can only concatenate str (not "int") to str

list1 = [1,2,3]
tuple1 = (1,2,5)
a = tuple1,list1
print(a) #((1, 2, 5), [1, 2, 3]) #タプルの中にリストを格納できる


name1,name2,name3,name4= '', 'suzuki','tanaka','sato'
selected_name = name1 or name2 or name3 or name4
print(selected_name) #suzuki

dive_into_code = ['Noro', 'Nakao', 'Miyaoka', 'Miyashita', 'Shibata', 'Kimura']
#dive_into_code.clear()
del dive_into_code[:]
print(dive_into_code)

dic = {'Noro': 1, 'Nakao': 2, 'Miyaoka': 3}

dic['Miyaoka'] += 1

print(dic)

list = [6,[5,[1,2]],4,[3,0]]

import reprlib
reprlib.repr(set('diveintocode'))

print(3*3.72/1.5)

def fugafuga(title,content = 'default_content', number = 4):
    content = 'content'
    print(title, end=' ')
    print(content, end=' ')
    print(number)
 
fugafuga(title = 'title_default', content = 'None', number = 5)

a = 2
b = 5

c = 3.0 + b, 5 * a

print(c)

class DiveIntoCode:
    def __init__(self, teacher, mentor):
        self.teacher = teacher
        self.mentor  = mentor

dic = DiveIntoCode('Noro', 'Miyaoka')
print(dic.teacher)
print(dic.mentor)

num_list  = [2, 4, 6, 4, 4, 2, 6]
print(num_list.count(10)) #0
print(num_list.count(4)) #3
for i in range(num_list.count(4)):
    print(i, end=' ')

print()

print("出力結果:")
try:
  raise Exception("開始前","Exception発生")
  print("開始")
except IOError as msg:
  print("IOError発生:",msg.args[0])
except Exception as msg:
  print("予期せぬ問題発生:",msg.args[0])
else:
  print("Else表示")

#出力結果:
#予期せぬ問題発生: 開始前

print("出力結果:")
try:
  raise Exception("開始前","Exception発生")
  print("開始")
except IOError as msg:
  print("IOError発生:",msg.args[0])
except Exception as msg:
  print("予期せぬ問題発生:",msg.args[1])
else:
  print("Else表示")

#出力結果:
#予期せぬ問題発生: Exception発生



  
