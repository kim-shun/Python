Zen = 'BeautifulIsBetterThanUgly'
print(Zen[1000:10000]) #エラーにはならない

import statistics
data = [1,10,15,20,25,30,35]
data2 = [1,10,15,20,25,30,35,40]
rslt1 = statistics.mean(data) #19.428571428571427　平均
rslt2 = statistics.median(data) #20　中央値
rslt3 = statistics.variance(data) #138.95238095238093　分散
rslt11 = statistics.mean(data2) #22
rslt22 = statistics.median(data2) #22.5
rslt33 = statistics.variance(data2) #172
#rslt4 = statistics.center(data)
#AttributeError: module 'statistics' has no attribute 'center'
#rslt5 = statistics.middle(data)
#AttributeError: module 'statistics' has no attribute 'middle'
#rslt6 = statistics.scatter(data)
#AttributeError: module 'statistics' has no attribute 'scatter'
#rslt7 = statistics.balance(data)
#AttributeError: module 'statistics' has no attribute 'balance'
#rslt8 = statistics.average(data)
#AttributeError: module 'statistics' has no attribute 'average'
print(rslt1)
print(rslt2)
print(rslt3)
print(rslt11)
print(rslt22)
print(rslt33)

import sys
print(dir(sys)) #いっぱい出てくる

#processing
#smtplib
#urllib.request

import glob
print(glob.glob('*.py')) #['test_0916.py']

import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
#['foot', 'fell', 'fastest']
print( re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
#cat in the hat
import math
c = math.cos(math.pi / 4)
l = math.log(1024,2)
print(c) #0.7071067811865476
print(l) #10.0



