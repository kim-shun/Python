from tkinter import *

count = 1

def click_count():
    global count
    txt.insert(0,count)

    def disable():
        txt.delete(1,END)
        if count >= 9:
            btn["state"] = "disable"
    disable()
    count += 1

win = Tk()
cv = Canvas(win, width = 300, height = 200)
win.title('クリック数をカウントする')
cv.pack()

txt = Entry(width = 1)
txt.place(x = 135, y = 50)

btn = Button(text='ボタン', command = click_count)
btn.place(x = 125, y = 100)
