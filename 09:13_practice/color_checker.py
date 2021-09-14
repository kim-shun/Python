from tkinter import *

def cal_hexa(num):
    nums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    hexa = ""
    while num:
        remainder = num % 16
        hexa = nums[remainder] + hexa
        num //= 16
    return hexa

def btn_click():
    num = int(txt.get())
    txt2.insert(0,cal_hexa(num))

# ウィンドウの作成
win = Tk()
cv = Canvas(win, width = 600, height = 400)
cv.pack()
win.title("10進数を16進数に変える")

x = 40
y = 80
for i in range(3):
    lab = Label(win, text = "color_10")
    cv.create_window(150, x, win=lab)
    lab2 = Label(win, text = "color_16")
    cv.create_window(150, y, win=lab2)

    txt = Entry(win)
    cv.create_window(150, x+20, win=txt)
    x += 100
    txt2 = Entry(win)
    cv.create_window(150, y+20, win=txt2)
    y += 100

cv.create_oval(550-20, 325-20, 300+20, 75+20, fill="red", outline="black")


#ボタンの作成
# ボタンの生成・描画
button = Button(text='確定', command=btn_click)
cv.create_window(150, 340, win=button)
