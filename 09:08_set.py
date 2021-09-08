a = {1,3,5,8}
b = {3,5,8,9}
print(a - b) #{1}
print(b - a) #{9}
print(a | b) #{1, 3, 5, 8, 9}
print(a & b) #{8, 3, 5}
print(a ^ b) #{1, 9}

print(a and b) #{8, 9, 3, 5}
print(a or b) #{8, 1, 3, 5} #重複不可、順序なし
#print(a && b) #invalid syntax

print(tuple(a)) #(8, 1, 3, 5) 順序つき、変更不可
print(list(a)) #[8, 1, 3, 5]

fruits = ['orange', 'banana','kiwi','apple']
a = ['X','Y','Z']
fruits[len(fruits):] = [a] #['orange', 'banana', 'kiwi', 'apple', ['X', 'Y', 'Z']]
#fruits.append(a) #['orange', 'banana', 'kiwi', 'apple', ['X', 'Y', 'Z']]
#fruits.extend(a) #['orange', 'banana', 'kiwi', 'apple', 'X', 'Y', 'Z']
#fruits.insert(2, 'ZZZ') #['orange', 'banana', 'ZZZ', 'kiwi', 'apple']
print(fruits)

fruits.insert(-99, 'PPPPPP')
print(fruits) #['PPPPPP', 'orange', 'banana', 'kiwi', 'apple', ['X', 'Y', 'Z']]
fruits.extend('apple')
print(fruits) #['PPPPPP', 'orange', 'banana', 'kiwi', 'apple', ['X', 'Y', 'Z'], 'a', 'p', 'p', 'l', 'e']
fruits.append('apple')
print(fruits) #['PPPPPP', 'orange', 'banana', 'kiwi', 'apple', ['X', 'Y', 'Z'], 'a', 'p', 'p', 'l', 'e', 'apple']
fruits.remove('apple')
print(fruits) #['PPPPPP', 'orange', 'banana', 'kiwi', ['X', 'Y', 'Z'], 'a', 'p', 'p', 'l', 'e', 'apple']
a = fruits.pop(2) #1個ずつ限定?
print(a) #banana
b = fruits[2]
print(b) #kiwi　前述でbananaが抜き去られている
c = fruits.pop()
print(c) #apple #最後尾が抜かれる
#fruits.clear() #[]
#del fruits[:] #[]
#del fruits #箱そのものがなくなる
print()
d = fruits.index('kiwi',0,4)
print(d) #2 2番目にkiwiが出てくる
e = fruits.index('a',2,11)
print(e) #4
print(fruits) #['PPPPPP', 'orange', 'kiwi', ['X', 'Y', 'Z'], 'a', 'p', 'p', 'l', 'e']
fruits.remove(['X', 'Y', 'Z'])

fruits.sort(key=None,reverse=True) #keyの指定もできる
print(fruits) #['p', 'p', 'orange', 'l', 'kiwi', 'e', 'a', 'PPPPPP']
fruits.reverse()
print(fruits) #['PPPPPP', 'a', 'e', 'kiwi', 'l', 'orange', 'p', 'p'] #元々のを逆にする
copyyy = fruits.copy()
print(copyyy)
