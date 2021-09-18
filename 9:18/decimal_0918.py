
def change_decimal(hexa):
    nums = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,
            '7':7,'8':8,'9':9,'A':10,'B':11,
            'C':12,'D':13,'E':14,'F':15}
    sum = 0
    for i in hexa:
        sum = 16 * sum + nums[i.upper()]
    return sum

try:
    hexa = input("16進数を入力してください(マイナス値が扱えません)：")
    result = change_decimal(hexa)
    print(result)
except KeyError:
    print('0～9の数字、A～Fの英字を半角で入力してください')

#Python標準機能の場合
print(int(hexa, 16))
    

