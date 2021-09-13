from tkinter import *

#ウィンドウの作成
win = Tk()
cv = Canvas(win, width = 600, height = 400)
cv.pack()

#ボールの位置サイズ
ball = {"dirx": 15, "diry": -15, "x": 450, "y": 300, "w": 10}

#オブジェクトを描画する
def draw_objects():
    #winを黄色バックにする
    cv.create_rectangle(0,0,600,400, fill="yellow",width=0)
    #ボールを描画
    cv.create_oval(ball["x"] - ball["w"],ball["y"] - ball["w"],
                   ball["x"] + ball["w"], ball["y"] + ball["w"], fill="black")

draw_objects()
win.mainloop()

