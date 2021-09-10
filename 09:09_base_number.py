def base_number(num):
    remainders = []
    while True:
        remainder = num % 2
        remainders.append(str(remainder))
        num //= 2
        if num == 0:
            remainders.reverse()
            binary = "".join(remainders)
            print("2進数は" + binary + "です")
            break
        '''
          2進数の値がString型になっています
        '''

num = int(input("数字を入力してください："))
base_number(num)

print()
print()
#Pythonの標準機能

num2 = 160
print(bin(num2))
#'0b10100000'

num3 = 160
print(format(num3, 'b'))
#'10100000'

num4 = 160
print('{:b}'.format(num4))
#'10100000'

num5 = 160
print(f'{num5:b}')
#'10100000'
