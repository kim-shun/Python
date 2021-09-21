from tkinter import *

def btn_click0():
    txt.insert(len(txt.get()),0)
    click_count()

def btn_click1():
    txt.insert(len(txt.get()),1)
    click_count()

def btn_click2():
    txt.insert(len(txt.get()),2)
    click_count()

def btn_click3():
    txt.insert(len(txt.get()),3)
    click_count()

def btn_click4():
    txt.insert(len(txt.get()),4)
    click_count()

def btn_click5():
    txt.insert(len(txt.get()),5)
    click_count()

def btn_click6():
    txt.insert(len(txt.get()),6)
    click_count()

def btn_click7():
    txt.insert(len(txt.get()),7)
    click_count()

def btn_click8():
    txt.insert(len(txt.get()),8)
    click_count()

def btn_click9():
    txt.insert(len(txt.get()),9)
    click_count()

def btn_click_a():
    txt.insert(len(txt.get()),'A')
    click_count()

def btn_click_b():
    txt.insert(len(txt.get()),'B')
    click_count()

def btn_click_c():
    txt.insert(len(txt.get()),'C')
    click_count()

def btn_click_d():
    txt.insert(len(txt.get()),'D')
    click_count()

def btn_click_e():
    txt.insert(len(txt.get()),'E')
    click_count()

def btn_click_f():
    txt.insert(len(txt.get()),'F')
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
    cv.create_oval(550-20, 325-20, 300+20, 75+20, fill="white", outline="black")
    txt2.insert(0,'6')
    global n
    n = 5

def escape():
    win.destroy()
    
    

win = Tk()
cv = Canvas(win, width = 600, height = 400)
win.title('ボールの色を変える')
cv.pack()

lbl = Label(text='回ボタンを押してください')
lbl.place(x=160, y=103)

lbl2 = Label(text='あと')
lbl2.place(x=110, y=103)

txt = Entry(width=6)
txt.place(x=110, y=140)
txt2 = Entry(width=1)
txt2.place(x=140, y=100)
txt2.insert(0,'6')

nums = '0123456789ABCDEF'

btn_clicks = [btn_click0,btn_click1,btn_click2,btn_click3,btn_click4,
              btn_click5,btn_click6,btn_click7,btn_click8,btn_click9,
              btn_click_a,btn_click_b,btn_click_c,btn_click_d,
              btn_click_e,btn_click_f]

x = 30
for i in range(16):
    btn = Button(text=nums[i],command=btn_clicks[i])
    cv.create_window(x, 50, win=btn)
    x += 30

cv.create_oval(550-20, 325-20, 300+20, 75+20, fill="white", outline="black")

color_btn = Button(win, text='カラーチェンジ', state='disable',command=color_change)
color_btn.place(x=110, y=200)

clear_btn = Button(win, text='クリア', command=clear)
clear_btn.place(x=110, y=240)

escape_btn = Button(win, text='終了', command=escape)
escape_btn.place(x=110, y = 280)



