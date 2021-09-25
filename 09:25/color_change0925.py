from tkinter import *


def btn_click():
    global btn
    txt.insert(len(txt.get()),1)




win = Tk()
cv = Canvas(win, width = 600, height = 400)
win.title('グローバル変数を用いる')
cv.pack()



txt = Entry(width=6)
txt.place(x=110, y=140)
txt2 = Entry(width=1)

hexa = "0123456789ABCDEF"

btns = []
x = 30
for i in range(16):
    btn = Button(text = hexa[i],command= btn_click)
    cv.create_window(x, 50, win=btn)
    btns.append(btn)
    x += 30



