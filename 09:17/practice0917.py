'''
import re
prog = re.compile('(K|S)us(a|u)n(a|o)(o|m)?g?i?(saya)?', re.IGNORECASE)
ret = prog.search('SUSANOO')
print(ret)
ret2 = prog.search('Kusaneiro')
print(ret2) #None
#?が0、または1回あるかどうかの確認
import math
print(math.e) #自然対数の底(ネイピア数) 2.718281828459045
print(math.exp(12)) #指数関数 162754.79141900392
print(math.log10(1024)) #対数関数 #3.010299956639812
print(math.log2(16)) #4.0


try:
    int_a = int(input('整数a:'))
    int_b = int(input('整数b:'))
    print(int_a ** 2)
    print((int_a ** 2) / int_b)
except(ZeroDivisionError) :
    print('C')
except(ValueError) :
    print('D')
except:
    print('E')
else:
    print('F')
finally:
    print('G')
'''


#David is a
#strategic
#AI

class wexal(Exception):
    pass

name = 'David'

def func(name: int):
    try:
        if name != 0:
            raise_his_character(name)
    except wexal:
        print('strategic')
        raise Exception

def raise_his_character(a):
    print(a, 'is a')
    raise wexal
    print('naughty boy')

try:
    func(name)
except Exception:
    print('AI')






