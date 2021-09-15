a = set('ameharekaze')
b = set('amedasu')
c = a ^ b
c2 = b ^ a #排他的論理和xor重複を取り除く
d = a & b
e = a | b
f = a - b
g = b - a
print(a) #{'m', 'e', 'r', 'a', 'z', 'k', 'h'}
print(c) #{'z', 'd', 'r', 's', 'u', 'h', 'k'}
print(c2) #cと同じ
print(d) #{'m', 'e', 'a'}
print(e) #{'m', 'e', 'h', 's', 'z', 'r', 'k', 'u', 'a', 'd'}
print(f) #{'r', 'z', 'h', 'k'}
print(g) #{'d', 's', 'u'}
def var_test():
    def do_variable():
        #nonlocal string
        global string
        #pass string
        string = 'today is not' #hot?
    string = 'today is cold'
    do_variable()
    print(string)
var_test() #today is not (nonlocal string)
#var_test() #invalid syntax (pass string)
#var_test() #today is cold (global string)

#globalは1番外側を参照
#nonlocalは関数の一つ外側を参照、値をキープできる

'''
docstring = documentation string
'''

import math
pi1 = math.pi #円周率
pow1 = math.pow(2,3) #べき乗
sqrt1 = math.sqrt(49) #平方根
print(pi1) #3.141592653589793
print(pow1) #8.0
print(sqrt1) #7.0

data = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
result = []
for i in range(4):
    for row in data:
        result.append(row[i])
print(result) #[1, 5, 9, 2, 6, 10, 3, 7, 11, 4, 8, 12]
        
#result = [[row[i] for row in data] for i in range(4)]
#print(result) #[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]



