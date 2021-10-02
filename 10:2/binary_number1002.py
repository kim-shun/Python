def binary_number(num):
    binary = ""
    while num:
        binary = str(num % 2) + binary
        num //= 2
    return binary
#print(0 % 2) #0
#90print(str(0 % 2) + "") #0
num = int(input("整数を入力してください："))
result = binary_number(num)
print(result)
