a = ['a','bbbbbb','','c','d']
print(len(a)) #5
n = [1,2,3]
x = [a,n]
print(x) #[['a', 'bbbbbb', '', 'ccc', 'd'], [1, 2, 3]]
print(x[0][1]) #bbbbbb
#print(x[2][0]) #エラー
print(len(x)) #2
print(len(x[1])) #3
print(len(x[0][1])) #6
#print(len(x[1][1])) #数字は数えられない
print(len(x[1])) #3
yy = "12345"
print(len(yy)) #5
xx = 12345
#print(len(xx)) #数字は数えられない

s = 'su\np\\'
print(s)
print(len(s)) #5　バックスラッシュだけ数えられない
t = "a          a"
print(len(t)) #12
aaa = '''
AAA

AAA
'''
print(len(aaa)) #10 文字が6個と改行コードが4個

tt,vv = 0, 1
print(tt) #0
print(tt,vv) #0 1
