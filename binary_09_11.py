'''
def binary(number):
    binary = str(number % 2)
    number //= 2
    while number > 0:
        #binary += str(number % 2) 逆順になる
        binary = str(number % 2) + binary
        number //= 2
    return binary

def main():
    number = int(input("数字を入力してください："))
    print(f"2進数は{binary(number)}です")

if __name__ == "__main__":
    main()


def base_number(num):
    return (base_number(num // 2) if num > 1 else '') + str(num % 2)

num = int(input("数字を入力してください："))
print("2進数は" + base_number(num) + "です")
'''

