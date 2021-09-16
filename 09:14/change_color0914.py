from tkinter import *

def btn_click0():
    txt.insert(count,0)

def btn_click1():
    txt.insert(count,1)

def btn_click2():
    txt.insert(count,2)

def btn_click3():
    txt.insert(count,3)

def btn_click4():
    txt.insert(count,4)

def btn_click5():
    txt.insert(count,5)

def btn_click6():
    txt.insert(count,6)

def btn_click7():
    txt.insert(count,7)

def btn_click8():
    txt.insert(count,8)

def btn_click9():
    txt.insert(count,9)

def btn_click_a():
    txt.insert(count,'A')

def btn_click_b():
    txt.insert(count,'B')

def btn_click_c():
    txt.insert(count,'C')
    limited_str()

def btn_click_d():
    txt.insert(count,'D')

def btn_click_e():
    txt.insert(count,'E')

def btn_click_f():
    txt.insert(count,'F')

win = Tk()
cv = Canvas(win, width = 600, height = 400)
win.title('ボールの色を変える')
cv.pack()

txt = Entry(width=20)
txt.place(x=90, y=100)
txt2 = Entry(width=20)
txt2.place(x=90, y=140)

count = 0
for i in range(16):
    btn_0 = Button(text='0',command=btn_click0)
    cv.create_window(30, 50, win=btn_0)
    btn_1 = Button(text='1',command=btn_click1)
    cv.create_window(60, 50, win=btn_1)
    btn_2 = Button(text='2',command=btn_click2)
    cv.create_window(90, 50, win=btn_2)
    btn_3 = Button(text='3',command=btn_click3)
    cv.create_window(120, 50, win=btn_3)
    btn_4 = Button(text='4',command=btn_click4)
    cv.create_window(150, 50, win=btn_4)
    btn_5 = Button(text='5',command=btn_click5)
    cv.create_window(180, 50, win=btn_5)
    btn_6 = Button(text='6',command=btn_click6)
    cv.create_window(210, 50, win=btn_6)
    btn_7 = Button(text='7',command=btn_click7)
    cv.create_window(240, 50, win=btn_7)
    btn_8 = Button(text='8',command=btn_click8)
    cv.create_window(270, 50, win=btn_8)
    btn_9 = Button(text='9',command=btn_click9)
    cv.create_window(300, 50, win=btn_9)
    btn_a= Button(text='A',command=btn_click_a)
    cv.create_window(330, 50, win=btn_a)
    btn_b = Button(text='B',command=btn_click_b)
    cv.create_window(360, 50, win=btn_b)
    btn_c = Button(text='C',command=btn_click_c)
    cv.create_window(390, 50, win=btn_c)
    btn_d = Button(text='D',command=btn_click_d)
    cv.create_window(420, 50, win=btn_d)
    btn_e = Button(text='E',command=btn_click_e)
    cv.create_window(450, 50, win=btn_e)
    btn_f = Button(text='F',command=btn_click_f)
    cv.create_window(480, 50, win=btn_f)
    count += 1
