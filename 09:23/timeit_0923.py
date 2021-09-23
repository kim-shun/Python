import timeit

def change_decimal(hexa): #【A】
    nums = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,
            '7':7,'8':8,'9':9,'A':10,'B':11,
            'C':12,'D':13,'E':14,'F':15}
    sum = 0
    for i in hexa:
        sum = 16 * sum + nums[i.upper()]
    return sum


HEXA = '0123456789ABCDEF'
def change_decimal2(hexa): #【B】
    return sum(HEXA.index(digit.upper()) * (16**n)
               for n, digit in enumerate(hexa[::-1]))

try:
    hexa = input("16進数を入力してください(マイナス値が扱えません)：")
    
    result = change_decimal(hexa)
    print("【A】：",result)
    print("処理にかかる時間は",timeit.timeit('change_decimal(hexa)',globals=globals()),"です")

    print()
    
    result2 = change_decimal2(hexa)
    print("【B】：",result2)
    print("処理にかかる時間は",timeit.timeit('change_decimal2(hexa)',globals=globals()),"です")

    print()
    
except KeyError:
    print('0～9の数字、A～Fの英字を半角で入力してください')


print("Python標準機能：",int(hexa, 16))
print("処理にかかる時間は",timeit.timeit('int(hexa, 16)',globals=globals()),"です")



