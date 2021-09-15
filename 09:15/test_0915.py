print('PHP' > 'Perl' > 'Python') #False
print('PHP' < 'Perl' < 'Python') #True
print('a' < 'b' < 'c') #True
print('B' < 'a' < 'c') #True 大文字優先

#enumerate
#deque
#pop
Zen = ['Simple','is','better','than','complex']
'''
print(Zen[0:5]) #['Simple', 'is', 'better', 'than', 'complex']
print(range(Zen[0:5])) #これがエラー
for i in range(Zen[0:5]):
    print(i, Zen[i])
#TypeError: 'list' object cannot be interpreted as an integer

for i in range(len(Zen)):
    print(i, Zen[i])

for i,v in enumerate(Zen):
    print(i,v)

0 Simple
1 is
2 better
3 than
4 complex
'''

nums = list(range(10))
print(nums[0:5])
#[0, 1, 2, 3, 4]
strs = ["A","B","C","D","E"]
print(strs[1:3])
#['B', 'C']

a = [1,3,4,6,3,5]
a.insert(3,-1)
print(a) #[1, 3, 4, -1, 6, 3, 5]
a.pop(4) #4番目を抜き取る
print(a) #[1, 3, 4, -1, 3, 5]
a.remove(3) #3という数字を取り除く
print(a) #[1, 4, -1, 3, 5]

matrix = [[2, 3, 5], [4, 9, 25], [8, 27, 125]]
power = [row[2] for row in matrix]
print(power) #[5, 25, 125]

matrix = [[1, 3, 5], [4, 9, 25], [8, 27, 125]]
'''
power = [[row[i] for row in matrix] for i in range(3)]
print(power) #[[1, 4, 8], [3, 9, 27], [5, 25, 125]]
'''
power = list(zip(matrix))
print(power) #[([1, 3, 5],), ([4, 9, 25],), ([8, 27, 125],)]
power = list(zip(*matrix))
print(power) #[(1, 4, 8), (3, 9, 27), (5, 25, 125)]

fruits = ['apple', 'kiwi', 'plum']
fruits.pop() #末尾を抜き取る
print(fruits) #['apple', 'kiwi']
aaa = [1,2,3,4,5,6,7,8]
aaa.pop() #末尾を抜き取る
print(aaa) #[1, 2, 3, 4, 5, 6, 7]

'''
Zena = 'BeautifulIsBetterThanUgly'
Zena[3] = "b"
print(Zena) #TypeError: 'str' object does not support item assignment
'''

matrix2 = [[2, 3, 5], [4, 9, 25], [8, 27, 125]]
power2 = [row[2] for row in matrix2]
print(power2)
