from tkinter import *

# ウィンドウの作成
win = Tk()
cv = Canvas(win, width = 600, height = 400)
cv.pack()

nums = list(range(10))

def btn_click():
    txt.insert(0,1)

# テキストボックス
txt = Entry(width=20)
txt.place(x=90, y=100)

# ボタンの作成
# ボタンの生成・描画
buttons = []
i = 30
for j in range(10):
    button = Button(text=str(nums[j]), command=btn_click)
    cv.create_window(i, 50, win=button)
    buttons.append(button)
    i += 60

print(buttons[0])
print(buttons[1])
print(buttons[2])

