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
