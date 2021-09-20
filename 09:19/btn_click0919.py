from tkinter import *

count = 1

def click_count():
    global count
    txt.insert(0,count)
    txt.delete(len(str(count)),END)
    count += 1

win = Tk()
cv = Canvas(win, width = 300, height = 200)
win.title('クリック数をカウントする')
cv.pack()

txt = Entry(width = 3)
txt.place(x = 130, y = 50)

btn = Button(text='ボタン', command = click_count)
btn.place(x = 125, y = 100)
