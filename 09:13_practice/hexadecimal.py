class HexEx(Exception):
    pass


def cal_hexa(num):
    #nums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    nums = '0123456789ABCDEF'
    hexa = ""
    while num:
        remainder = num % 16
        hexa = nums[remainder] + hexa
        num //= 16
    return hexa

try:
    num = int(input("整数を入力してください："))
    if num < 0:
        raise HexEx("マイナスは対象外です")
    result = cal_hexa(num)
    print(result)
except HexEx as e:
    print(e)

#0だと表示されない
#負数だと無限ループになる

#Python標準機能の場合
print(hex(num))

'''
def cal_hexa2(num2):
    return (cal_hexa(num // 16) if num >= 16 else '') + '0123456789ABCDEF'[num % 16]

num2 = int(input("整数を入力してください："))
result2 = cal_hexa(num2)
print(result2)
'''
