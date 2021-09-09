def base_number(num):
    remainders = []
    while True:
        remainder = num % 2
        remainders.append(str(remainder))
        num //= 2
        if num == 0:
            binary = "".join(remainders)
            print("2進数は" + binary + "です")
            break
        '''
        2進数の値がString型になっています
        '''

num = int(input("数字を入力してください："))

base_number(num)
