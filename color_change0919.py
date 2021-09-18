from tkinter import *

def btn_click():
    txt.insert(7,0)
    click_count()


n = 5

def click_count():
    global n
    txt2.insert(0,n)
    if n == 3 or n == 0:
        color_btn["state"] = "normal"
    else:
        color_btn["state"] = "disable"    
    n -= 1
    txt2.delete(1, END)
        

def color_change():
    hexa = txt.get()
    color = '#' + hexa
    cv.create_oval(550-20, 325-20, 300+20, 75+20, fill=color, outline="black")

def clear():
    txt.delete(0, END)
    txt2.delete(0, END)
    color_btn["state"] = "disable"
    txt2.insert(0,'6')
    global n
    n = 5
    
    

win = Tk()
cv = Canvas(win, width = 600, height = 400)
win.title('ボールの色を変える')
cv.pack()

lbl = Label(text='回ボタンを押してください')
lbl.place(x=160, y=103)

lbl = Label(text='あと')
lbl.place(x=110, y=103)

txt = Entry(width=6)
txt.place(x=110, y=140)
txt2 = Entry(width=1)
txt2.place(x=140, y=100)
txt2.insert(0,'6')

nums = '0123456789ABCDEF'

x = 30
for i in range(16):
    btn = Button(text=nums[i],command=btn_click)
    cv.create_window(x, 50, win=btn)
    x += 30

    
color = "white"
cv.create_oval(550-20, 325-20, 300+20, 75+20, fill=color, outline="black")

color_btn = Button(win, text='カラーチェンジ', state='disable',command=color_change)
color_btn.place(x=110, y=200)

clear_btn = Button(win, text='クリア', command=clear)
clear_btn.place(x=110, y=240)

