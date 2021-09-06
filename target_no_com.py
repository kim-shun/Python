# target_a_no_com
# ボール移動
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
        ball["x"] + ball["w"], ball["y"] + ball["w"], fill="yellow")

# ボールの移動
def move_ball():
    global is_gameover, point
    if is_gameover: return
    bx = ball["x"] + ball["dirx"]
    by = ball["y"] + ball["diry"]
    # 上左右の壁に当たった？
    if bx < 0 or bx > 600: ball["dirx"] *= -1
    if by < 0: ball["diry"] *= -1

    # ゲームオーバー？
    if by >= 400:
        win.title("画面の下に到達しました！")
        is_gameover = True
    if 0 <= bx <= 600: ball["x"] = bx
    if 0 <= by <= 400: ball["y"] = by

def game_loop():
    draw_objects()
    move_ball()
    win.after(250, game_loop)

# マウスイベントの処理
def click(e): # クリックでリスタート
    if is_gameover: init_game()
# マウスイベントを登録
win.bind('<Button-1>', click) # マウスの左クリック
# ゲームのメイン処理
init_game()
game_loop()
win.mainloop()
