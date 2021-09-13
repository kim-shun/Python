word = "Python"
print(word[:4] + word[4:]) #Python
print(word[:2] + word[2:]) #Python
print(word[4:42]) #on
print(word[2:5]) #tho
a = "Hello Python"
print(a) #Hello Python
print(3 * a[3]) #lll
print(word[0],word[2]) #P t
print(word[1:4] * 2) #ythyth
print(word[:2] + word[-2:]) #Pyon
print(word[:3]) #Pyt 最初から3まで (3を含まない)
print(word[3:]) #hon　3から最後まで (3を含まない)
print(word[42:4]) # 空白
print(2 * word[1:4] + word[0]) #ythythP
print(word[-6:]) #Python
print(word[0:]) #Python 0から最後まで
print(word[:]) #Python 最初から最後まで
print(word[:100]) #Python　最初から100まで (エラー起きない)
print(word[-99:]) #Python　-99から最後まで (エラー起きない)
print(word[:2] + '*_*' + word[-2:]) #Py*_*on
print(word[1] + '' + word[2]) #yt ただ足し算したのと同じ
print(word * 3) #PythonPythonPython
print(word[1:1]) #空白

s = 'supercalifragilisticexpialidocious'
print(len(s)) #34
t = len(s)
u = 'super\npower'
print(u)
print(len(u)) #11

squares = [1, 4, 9, 16, 25]
print(squares) #[1, 4, 9, 16, 25]
print(squares[0]) #1
#print(squares[-9]) #オーバーしているため、エラーが起こる
print(squares[0:2]) #[1, 4]
print(squares[:9]) #オーバーしていても対応可能 [1, 4, 9, 16, 25]
print(squares[-9:99]) #[1, 4, 9, 16, 25]
print(squares + [36,49,64,81,100]) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares2 = [306, 49, 64, 81, 100]
print(squares, squares2) #[1, 4, 9, 16, 25] [306, 49, 64, 81, 100]
print(squares * 2) #[1, 4, 9, 16, 25, 1, 4, 9, 16, 25]
