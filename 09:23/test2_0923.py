#バイナリデータレコードの処理を行うモジュール：struct

import json
x = {'name':'yamada','data':[2,3,4]}
print(json.dumps(x))

i = 10

def num(arg=i):
    print(arg)

i = 7

num()

member = {1: 'Noro', 2: 'Nakao', 3: 'Miyaoka'}
member[4] = 'Kimura'
del member[3]
print(list(member.keys()))

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#このユーザー定義例外は、Exceptionクラスのデフォルトの__init__をオーバーライドしている。
#【誤】このユーザー定義例外では.args属性は存在しない。
#【誤】このユーザー定義例外を直接プリントしても値は返ってこない。
#【誤】このユーザー定義例外の.value属性はタプルである。

d = 'diveinto'

d + 'code'

print(d)


import math
math.cos(math.pi / 5)

print("出力結果:")
print('円周率は%5.3fである。'%math.pi)

class Sample:

  c_list = []

  def add_c_list(self,data):
    self.c_list.append(data)

print("出力結果:", end=" ")
sample1 = Sample()
sample1.add_c_list("データ1")

sample2 = Sample()
sample2.add_c_list("データ2")

for item_data in sample1.c_list:
  print(item_data, end=" ")

#出力結果: データ1 データ2
