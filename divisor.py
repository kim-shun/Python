'''
def divisor(num):
    nums = []
    for i in range(1,num + 1):
        if num % i == 0:
            nums.append(i)
    return nums
num = int(input("数字を入力してください："))
print(divisor(num))
'''

num = int(input("約数の総和を出したい整数を入力してください："))
divisor_range = int(input("和を出したい約数の範囲を指定してください"))
divisor = [i for i in range(1,num + 1) if num % i == 0]
limited_divisor = [i for i in range(1,divisor_range + 1) if num % i == 0]
divisor_length = len(divisor)
divisor_sum = sum(divisor)

print("約数の数は" + str(divisor_length) + "です")
print(str(num) + "の約数の総和は" + str(divisor_sum) + "です")
print(str(divisor_range) + "以下の約数の和は" + str(sum(limited_divisor)) + "です")

