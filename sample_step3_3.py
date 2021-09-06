# sample_step3_03
from tkinter import *

# ウィンドウの作成
win = Tk()
cv = Canvas(win, width = 800, height = 600)
cv.pack()

# ボールの位置サイズ
ball = {"dirx": 150, "diry": -150, "x": 450, "y": 300, "w": 10}

# オブジェクトを描画する
def draw_objects():
    # winを黒バックにする
    cv.create_rectangle(0, 0, 800, 600, fill="green", width=0)
    # ボールを描画
    cv.create_oval(ball["x"] - ball["w"], ball["y"] - ball["w"],
        ball["x"] + ball["w"], ball["y"] + ball["w"], fill="red")

# ボールの移動
def move_ball():
    ball["x"]  = ball["x"] + ball["dirx"]
    ball["y"]  = ball["y"] + ball["diry"]

draw_objects()
move_ball()
draw_objects()
win.mainloop()
