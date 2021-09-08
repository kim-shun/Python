def f(a, L=[]):
    L.append(a ** 4)
    return L

#obj = f(4,[5])
#print(obj)
print(f(1)) #[1]
print(f(7)) #[1, 2401]
print(f(3)) #[1, 2401, 81]
#rubyとは違って呼び出される都度増える

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f2(1)) #[1]
print(f2(7)) #[7]
print(f2(3)) #[3]

#その都度初期化される

print(f2(4,L=[5])) #[5,4]

def parrot(v, st='a stiff',action='voom',ty='ノルウェージャンブルー'):
    print('アクション表示-->',action, end=' ')
    print('ボルテージ表示-->',v,'その後')
    print('タイプ表示-->',ty)
    print('ST表示-->',st,'!')
    print(v,st,action,ty)

#parrot('ボルテージ','2個目', '3個目', '4個目')

'''
アクション表示--> 3個目 ボルテージ表示--> ボルテージ その後
タイプ表示--> 4個目
ST表示--> 2個目 !
ボルテージ 2個目 3個目 4個目
'''
#parrot('ボルテージ',action='3個目',st='2個目')

'''
アクション表示--> 3個目 ボルテージ表示--> ボルテージ その後
タイプ表示--> ノルウェージャンブルー
ST表示--> 2個目 !
ボルテージ 2個目 3個目 ノルウェージャンブルー
'''
parrot('A', action='3個目')

'''
アクション表示--> 3個目 ボルテージ表示--> A その後
タイプ表示--> ノルウェージャンブルー
ST表示--> a stiff !
A a stiff 3個目 ノルウェージャンブルー
'''


