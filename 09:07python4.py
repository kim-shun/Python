'''
i = 5

def f(arg= i):
    #docstring(関数の説明文)
    print(arg)

i = 6
print(i) #6
f() #5
#変数のスコープ
'''


def culculate_average(a,b,c,d,e,f,g):
    average = (a + b + c + d + e + f + g) / 7
    return average

result = culculate_average(2,3,4,5,6,7,8)
print("平均は",result,"です")
    
