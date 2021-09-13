# クリックイベント
def btn_click():
    # テキスト取得
    num = int(txt_1.get())
    # 16進数へ変換してテキストボックスへセット
    txt_2.insert(0, hex(num))

import tkinter

# 画面作成
tki = tkinter.Tk()
tki.geometry('300x200')
tki.title('ボタンイベントの検証')

# ラベル
lbl_1 = tkinter.Label(text='10進数')
lbl_1.place(x=30, y=70)
lbl_2 = tkinter.Label(text='16進数')
lbl_2.place(x=30, y=100)

# テキストボックス
txt_1 = tkinter.Entry(width=20)
txt_1.place(x=90, y=70)
txt_2 = tkinter.Entry(width=20)
txt_2.place(x=90, y=100)

# ボタン
btn = tkinter.Button(tki, text='計算', command=btn_click)
btn.place(x=140, y=170)

# 画面をそのまま表示
tki.mainloop()
