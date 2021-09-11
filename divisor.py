def divisor(num):
    nums = []
    for i in range(1,num + 1):
        if num % i == 0:
            nums.append(i)
    return nums
num = int(input("数字を入力してください："))
print(divisor(num))
