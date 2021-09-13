from tkinter import *
'''
root = Tk()

def leftClick(event):
    print('Left')

def middleClick(event):
    print('Middle')

def rightClick(event):
    print('Right')

frame = Frame(root, width=300, height=250)
frame.bind('<Button-1>', leftClick)
frame.bind('<Button-2>', middleClick)
frame.bind('<Button-3>', rightClick)
frame.pack()

root.mainloop()
'''
# ウィンドウの作成
win = Tk()
cv = Canvas(win, width = 600, height = 400)
cv.pack()


# 入力ボックスの生成・描画
#entry = Entry (win)
#cv.create_window(270, 100, win=entry)

# ボタン押下時の処理定義
def btn_click1():
    n = 1
    txt.insert(0,n)
    cv.create_window(0, 160, win=label)
def btn_click2():
    n = 2
    txt.insert(0,n)
    cv.create_window(0, 160, win=label)
def btn_click3():
    n = 3
    txt.insert(0,n)
    cv.create_window(0, 160, win=label)
def btn_click4():
    n = 4
    txt.insert(0,n)
    cv.create_window(0, 160, win=label)
def btn_click5():
    n = 5
    txt.insert(0,n)
    cv.create_window(0, 160, win=label)
def btn_click6():
    n = 6
    txt.insert(0,n)
    cv.create_window(0, 160, win=label)
def btn_click7():
    n = 7
    txt.insert(0,n)
    cv.create_window(0, 160, win=label)
def btn_click8():
    n = 8
    txt.insert(0,n)
    cv.create_window(0, 160, win=label)
def btn_click9():
    n = 9
    txt.insert(0,n)
    cv.create_window(0, 160, win=label)
def btn_click0():
    n = 0
    txt.insert(0,n)
    cv.create_window(0, 160, win=label)


# テキストボックス
txt = Entry(width=20)
txt.place(x=90, y=100)

# ボタンの作成
# ボタンの生成・描画
button = Button(text='1', command=btn_click1)
cv.create_window(30, 50, win=button)
button = Button(text='2', command=btn_click2)
cv.create_window(90, 50, win=button)
button = Button(text='3', command=btn_click3)
cv.create_window(150, 50, win=button)
button = Button(text='4', command=btn_click4)
cv.create_window(210, 50, win=button)
button = Button(text='5', command=btn_click5)
cv.create_window(270, 50, win=button)
button = Button(text='6', command=btn_click6)
cv.create_window(330, 50, win=button)
button = Button(text='7', command=btn_click7)
cv.create_window(390, 50, win=button)
button = Button(text='8', command=btn_click8)
cv.create_window(450, 50, win=button)
button = Button(text='9', command=btn_click9)
cv.create_window(510, 50, win=button)
button = Button(text='0', command=btn_click0)
cv.create_window(570, 50, win=button)
