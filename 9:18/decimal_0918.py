def cal_decimal(hexa):
    nums = '0123456789ABCDEF'
    n = len(hexa)
    num_sum = 0
    for i in range(n):
        num = int(hexa[i]) * (16**(n - 1))
        num_sum += num
        n -= 1
    return num_sum


hexa = input("16進数を入力してください：")
result = cal_decimal(hexa)
print(result)
