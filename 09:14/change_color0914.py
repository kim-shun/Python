from tkinter import *

def color_change(num):
    color = num
    cv.create_oval(ball["x"] - ball["w"], ball["y"] - ball["w"],
    ball["x"] + ball["w"], ball["y"] + ball["w"], fill=color)

def btn_click0():
    txt1.insert(count,0)

def btn_click1():
    txt1.insert(count,1)

def btn_click2():
    txt1.insert(count,2)

def btn_click3():
    txt1.insert(count,3)

def btn_click4():
    txt1.insert(count,4)

def btn_click5():
    txt1.insert(count,5)

def btn_click6():
    txt1.insert(count,6)

def btn_click7():
    txt1.insert(count,7)

def btn_click8():
    txt1.insert(count,8)

def btn_click9():
    txt1.insert(count,9)



def btn_click():
    num = txt1.get()
    color_change('#' + num)
    

ball = {"dirx": 15, "diry": -15, "x": 450, "y": 200, "w": 80}
nums = '0123456789ABCDEF'
count = 0
i = 30
for j in range(10):
    if j == 0:
        button = Button(text=nums[j],command=btn_click0)
    elif j == 1:
        button = Button(text=nums[j],command=btn_click1)
    elif j == 2:
        button = Button(text=nums[j],command=btn_click2)
    elif j == 3:
        button = Button(text=nums[j],command=btn_click3)
    elif j == 4:
        button = Button(text=nums[j],command=btn_click4)
    elif j == 5:
        button = Button(text=nums[j],command=btn_click5)
    elif j == 6:
        button = Button(text=nums[j],command=btn_click6)
    elif j == 7:
        button = Button(text=nums[j],command=btn_click7)
    elif j == 8:
        button = Button(text=nums[j],command=btn_click8)
    elif j == 9:
        button = Button(text=nums[j],command=btn_click9)
    cv.create_window(i, 50, win=button)
    count += 1
    i += 60

win = Tk()
win.title("ボールの色を変える")
cv = Canvas(win, width = 600, height = 400)
cv.pack()

color = "white"

cv.create_oval(ball["x"] - ball["w"], ball["y"] - ball["w"],
    ball["x"] + ball["w"], ball["y"] + ball["w"], fill=color)

txt1 = Entry(width=10)
txt1.place(x=150, y=160)


btn = Button(text='カラーチェンジ', command=btn_click)
btn.place(x=150, y=220)
