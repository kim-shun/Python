from tkinter import *

def btn_click0():
    txt.insert(5,0)
    click_count()

def btn_click1():
    txt.insert(5,1)
    click_count()

def btn_click2():
    txt.insert(5,2)
    click_count()

def btn_click3():
    txt.insert(5,3)
    click_count()

def btn_click4():
    txt.insert(5,4)
    click_count()

def btn_click5():
    txt.insert(5,5)
    click_count()

def btn_click6():
    txt.insert(5,6)
    click_count()

def btn_click7():
    txt.insert(5,7)
    click_count()

def btn_click8():
    txt.insert(5,8)
    click_count()

def btn_click9():
    txt.insert(5,9)
    click_count()

def btn_click_a():
    txt.insert(5,'A')
    click_count()

def btn_click_b():
    txt.insert(5,'B')
    click_count()

def btn_click_c():
    txt.insert(5,'C')
    click_count()

def btn_click_d():
    txt.insert(5,'D')
    click_count()

def btn_click_e():
    txt.insert(5,'E')
    click_count()

def btn_click_f():
    txt.insert(5,'F')
    click_count()

n = 5

def click_count():
    global n
    txt2.insert(0,str(n))
    n -= 1
    txt2.delete(1, END)

def color_change():
    hexa = txt.get()
    color = '#' + hexa
    cv.create_oval(550-20, 325-20, 300+20, 75+20, fill=color, outline="black")  

def clear():
    txt.delete(0, END)
    txt2.delete(0, END)
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


try:
    btn = Button(text='0',command=btn_click0)
    cv.create_window(30, 50, win=btn)
    btn = Button(text='1',command=btn_click1)
    cv.create_window(60, 50, win=btn)
    btn = Button(text='2',command=btn_click2)
    cv.create_window(90, 50, win=btn)
    btn = Button(text='3',command=btn_click3)
    cv.create_window(120, 50, win=btn)
    btn = Button(text='4',command=btn_click4)
    cv.create_window(150, 50, win=btn)
    btn = Button(text='5',command=btn_click5)
    cv.create_window(180, 50, win=btn)
    btn = Button(text='6',command=btn_click6)
    cv.create_window(210, 50, win=btn)
    btn = Button(text='7',command=btn_click7)
    cv.create_window(240, 50, win=btn)
    btn = Button(text='8',command=btn_click8)
    cv.create_window(270, 50, win=btn)
    btn = Button(text='9',command=btn_click9)
    cv.create_window(300, 50, win=btn)
    btn= Button(text='A',command=btn_click_a)
    cv.create_window(330, 50, win=btn)
    btn = Button(text='B',command=btn_click_b)
    cv.create_window(360, 50, win=btn)
    btn = Button(text='C',command=btn_click_c)
    cv.create_window(390, 50, win=btn)
    btn = Button(text='D',command=btn_click_d)
    cv.create_window(420, 50, win=btn)
    btn = Button(text='E',command=btn_click_e)
    cv.create_window(450, 50, win=btn)
    btn = Button(text='F',command=btn_click_f)
    cv.create_window(480, 50, win=btn)
    

    color = "white"
    cv.create_oval(550-20, 325-20, 300+20, 75+20, fill=color, outline="black")


    color_btn = Button(win, text='カラーチェンジ', command=color_change)
    color_btn.place(x=110, y=200)

    clear_btn = Button(win, text='クリア', command=clear)
    clear_btn.place(x=110, y=240)
except Exception:
    pass

