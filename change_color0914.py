from tkinter import *

# ゲーム中で使う変数(配列)
blocks = []
# ボールの位置サイズ
ball = {"dirx": 15, "diry": -15, "x": 450, "y": 300, "w": 10}

# ウィンドウの作成
win = Tk()
cv = Canvas(win, width = 600, height = 400)
cv.pack()

# ゲームの初期化
def init_game():
    global is_gameover
    is_gameover = False
    win.title("ボール移動中！")
    ball["y"] = 250
    ball["diry"] = -10

# オブジェクトを描画する
def draw_objects():
    cv.delete('all') # 既存の描画を破棄
    cv.create_rectangle(0, 0, 600, 400, fill="black", width=0)
    # ボールを描画
    cv.create_oval(ball["x"] - ball["w"], ball["y"] - ball["w"],
        ball["x"] + ball["w"], ball["y"] + ball["w"], fill="#00ff00")
