import random
'''
num1 = random.choice(range(100))
num2 = random.choice(range(100))
print(num1, "+", num2,"=")
while True:
    answer = int(input("答えを入力してください："))
    if answer == num1 + num2:
        print("正解です")
        break
    else:
        print("間違いです")
'''


rand = random.choice(range(100))
count = 0
while True:
    answer = int(input("数を当ててください："))
    if answer == rand:
        print("正解です")
        count += 1
        print("あなたは",count,"回目で当てました")
        break
    elif abs(answer - rand) <= 10:
        print("惜しい")
        count += 1
    elif answer < rand:
        print("もっと大きいよ")
        count += 1
    elif answer > rand:
        print("もっと小さいよ")
        count += 1


'''
s = random.sample(range(100),10)
print(s)
r = random.random()
print(r)
rr = random.randrange(100)
'''

