import random
num1 = random.choice(list(range(100)))
num2 = random.choice(list(range(100)))
print(num1, "+", num2,"=")
while True:
    answer = int(input("答えを入力してください："))
    if answer == num1 + num2:
        print("正解です")
        break
    else:
        print("間違いです")




'''
s = random.sample(range(100),10)
print(s)
r = random.random()
print(r)
rr = random.randrange(100)
'''

