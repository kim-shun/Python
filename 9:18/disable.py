import tkinter

root = tkinter.Tk()

#ボタンクリック時に実行する関数
def disable_clicked():
    count_num = b["text"] +1    #クリック回数をカウント
    b["text"] = count_num       #ボタンに表示

    #10に到達したらdisableに設定
    if count_num == 10:
        b["state"] = "disable"  #無効化


#ボタン
b = tkinter.Button(
    root,
    width=15,
    text=0,         #初期値
    command=disable_clicked,    #クリック時に実行する関数
)
b.pack()

root.mainloop()
