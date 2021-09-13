import tkinter

def calculate_binary(num):
    binary = ""
    while num:
        remainder = str(num % 2)
        binary = remainder + binary
        num //= 2
    return binary
    
def btn_click():
    num = int(txt_1.get())
    txt_2.insert(0,calculate_binary(num))

def clear():
    txt_1.delete(0, tkinter.END)
    txt_2.delete(0, tkinter.END)


def escape():
    tki.destroy()

tki = tkinter.Tk()
tki.geometry('400x400')
tki.title('10進数を2進数に変える')

lbl_1 = tkinter.Label(text='10進数')
lbl_1.place(x=30, y=70)
lbl_2 = tkinter.Label(text='2進数')
lbl_2.place(x=30, y=100)

txt_1 = tkinter.Entry(width=20)
txt_1.place(x=90, y=70)
txt_2 = tkinter.Entry(width=20)
txt_2.place(x=90, y=100)

btn = tkinter.Button(tki, text='計算', command=btn_click)
btn.place(x=110, y=140)
clear_btn = tkinter.Button(tki, text='クリア', command=clear)
clear_btn.place(x=110, y=170)
escape_btn = tkinter.Button(tki, text='終了', command=escape)
escape_btn.place(x=110, y = 200)

tki.mainloop()
