'''
import shutil as mrt
mrt.copyfile('kisyou.db','tenki00.db')
'''

scores = [40,50,70,90,60]
it = iter(scores)
print(next(it),end=',')
print(next(it),end=',')
print('hello',end=',')
print(next(it),end=',')
#40,50,hello,70, 順番に取り出す

#regexp
#pattern
print()

import json
x = {'name':'yamada','data':[2,3,4]}
print(x) #{'name': 'yamada', 'data': [2, 3, 4]}
print(json.dumps(x)) #{"name": "yamada", "data": [2, 3, 4]}　ダブルクォーテーション
#シリアライズ、直列化、バイト列に変換
#print(json.load(x)) #AttributeError: 'dict' object has no attribute 'read'
print("-3.14".zfill(7)) #-003.14
s = '1234'
print(s.zfill(10)) #0000001234
t = 1234
#print(t.zfill(8)) #AttributeError: 'int' object has no attribute 'zfill'
#sysname
#release
#version

import glob
import re
import os

file = glob.glob('test/*.txt')
print(file) #[]
