'''
a = int(input("数字を入力してください："))
if a >= 80:
    print("合格")
elif a >= 70:
    print("おしい!")
else:
    print("ガンバレ!")
print("処理終了")


x = int(input("整数を入れてください："))
if x < 0:
    x = 0
    print('負数はゼロとする')
elif x == 0:
    print("ゼロ")
elif x == 1:
    print("1つ")
else:
    print("もっと")



words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))

for i in range(5):
    print(i)

'''

a, b, c = 2, 5, 7

if a < b != c: #pythonは「and」と「or」。「&&」と「||」は使えない
    print("True")
else:
    print("False")

print("END")

#対話型で'aaaa' < 'bb' < 'cc'と入力すると「True」と表示される
#'ba' < 'bbb' < 'cc'も「True」
#'aa' < 'aaa' < 'aaaa'も「True」
#'ca' < 'bb' < 'ac'は「False」、最初の1文字で判断される?

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print(sum(range(4))) #6 (0 + 1 + 2 + 3)
print(list(range(4))) #[0, 1, 2, 3]

x = [0,1,2,3,4] #range(5)はこのxを生成しているのと同じ

for i in x: #xをrange(5)にしても出力結果は同じ
    print(i)

for i in range(-10, 2):
    print(i)

for i in range(0, 10, 3): #3ずつ増える
    print(i)

for i in range(-10, -100, -30): #-10, -40, -70
    print(i)

        
