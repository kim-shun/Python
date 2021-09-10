import random

while True:
    jan = ["グー","チョキ","パー"]
    
    cpu = random.choice(jan)
    user = int(input("グーだったら0、チョキだったら1、パーだったら2を入力してください："))
    print("あなた：" + jan[user])
    print("CPU：" + cpu)

    if jan[user] == cpu:
        print("あいこです")
        continue
    else:
        if cpu == jan[user - 1]:
            print("負けです")
            break
        else:
            print("勝ちです")
            break

'''
jan[0] == "グー", jan[1] == "チョキ", jan[2] == "パー"(jan[-1] == "パー")

ユーザーが入力する値(0,1,2)をjan配列の添字にする
'''

