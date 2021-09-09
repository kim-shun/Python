def base_number(num):
    while True:
        remainder = num % 2
        print(remainder)
        num //= 2
        if num == 0:
            break

num = int(input("数字を入力してください："))

base_number(num)
