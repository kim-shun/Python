from tkinter import *

win = Tk()
cv = Canvas(win, width = 600, height = 400)
cv.pack()

nums = list(range(10))


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

def calculate():
    num = txt.get()
    txt2.insert(0,format(int(num), 'b'))

def clear():
    txt.delete(0, END)
    txt2.delete(0, END)

def escape():
    win.destroy()

lbl_1 = Label(text='10進数')
lbl_1.place(x=30, y=100)
lbl_2 = Label(text='2進数')
lbl_2.place(x=30, y=140)

txt = Entry(width=20)
txt.place(x=90, y=100)
txt2 = Entry(width=20)
txt2.place(x=90, y=140)

btn = Button(text='計算',command=calculate)
btn.place(x=110, y=180)

clear_btn = Button(text='クリア', command=clear)
clear_btn.place(x=110, y=220)

escape_btn = Button(text='終了', command=escape)
escape_btn.place(x=110, y = 250)

count = 0
i = 30
for j in range(10):
    if j == 0:
        button = Button(text=str(nums[j]),command=btn_click0)
    elif j == 1:
        button = Button(text=str(nums[j]),command=btn_click1)
    elif j == 2:
        button = Button(text=str(nums[j]),command=btn_click2)
    elif j == 3:
        button = Button(text=str(nums[j]),command=btn_click3)
    elif j == 4:
        button = Button(text=str(nums[j]),command=btn_click4)
    elif j == 5:
        button = Button(text=str(nums[j]),command=btn_click5)
    elif j == 6:
        button = Button(text=str(nums[j]),command=btn_click6)
    elif j == 7:
        button = Button(text=str(nums[j]),command=btn_click7)
    elif j == 8:
        button = Button(text=str(nums[j]),command=btn_click8)
    elif j == 9:
        button = Button(text=str(nums[j]),command=btn_click9)
    cv.create_window(i, 50, win=button)
    count += 1
    i += 60
    
