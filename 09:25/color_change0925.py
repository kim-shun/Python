from tkinter import *


def btn_click():
    global n
    txt.insert(len(txt.get()),n[1])




win = Tk()
cv = Canvas(win, width = 600, height = 400)
win.title('グローバル変数を用いる')
cv.pack()



txt = Entry(width=6)
txt.place(x=110, y=140)
txt2 = Entry(width=1)

n = [0,1,2,3]

btn = Button(text=str(n[1]),command=btn_click)
cv.create_window(30, 50, win=btn)



