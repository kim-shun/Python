#問題を表示
#問題を作成
#入力してもらう
#正解かどうかを判定
'''
def culc(a, b=1, squares=[], cubes=[]):
    print(squares)
    squares.append(a ** 2)
    print(squares)
    cubes.append(b ** 3)
    print(squares)
    return squares, cubes

#print(culc(1)) #([1], [1])
#print(culc(2, 3)) #([1, 4], [1, 27])
print(culc(3, 4)) #([1, 4, 9], [1, 27, 64])
#print(culc(4, 5)) #([1, 4, 9, 16], [1, 27, 64, 125])

a = ['dog','cat','tiger','horse','monkey']
for s in a[:]:
	if len(s) == 5:
		a.append(s)
print(a)
'''

'''
words = ['dog','monkey','cat','horse']
for i in words:
    print(len(i))
    if len(i) >= 5:
        print(i,end= ",")
'''
        
