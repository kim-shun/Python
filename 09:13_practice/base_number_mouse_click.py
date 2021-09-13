from tkinter import *

# ウィンドウの作成
win = Tk()
cv = Canvas(win, width = 600, height = 400)
cv.pack()

nums = list(range(10))

def btn_click():
    for i in range(10):
        txt.insert(0,i)

# テキストボックス
txt = Entry(width=20)
txt.place(x=90, y=100)

# ボタンの作成
# ボタンの生成・描画
i = 30
for j in range(10):
    button = Button(text=str(nums[j]), command=btn_click)
    cv.create_window(i, 50, win=button)
    i += 60



