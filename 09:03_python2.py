s = [1, 4, 9, 16, 25]

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
cubes.append(216)
cubes.append(7 ** 3)
print(cubes) #[1, 8, 27, 64, 125, 216, 343]
letters = ['a','b','c','d','e','f','g']
print(letters) #['a', 'b', 'c', 'd', 'e', 'f', 'g'] #イングルクォーテーションがデフォルト？
print(letters[2]) #c
letters[2:5] = []
print(letters) #['a', 'b', 'f', 'g']
print(letters[2:4]) #['f', 'g']
letters2 = ['a','b',55,'d','e',        'f','g']
print(letters2[2:4]) #[55, 'd']
print(letters2) #['a', 'b', 'c', 'd', 'e', 'f', 'g']
#PEP8(ルールブック)　半角の調整してくれたりする
letters2[2:5] = ['C', 'D', 'E']
print(letters2[:]) #['a', 'b', 'C', 'D', 'E', 'f', 'g']
letters2[2:5] = ['C']
print(letters2[:]) #['a', 'b', 'C', 'f', 'g'] EとDがなくなる
letters3 = ['a','b','c','d','e', 'f','g']
letters3[2:4] = ['C','D','E','E','E','E','E','E','E']
print(letters3) #['a', 'b', 'C', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'e', 'f', 'g']
print(letters3[6]) #E
letters3[4:10] = []
print(letters3[:]) #['a', 'b', 'C', 'D', 'E', 'e', 'f', 'g']
letters3[5] = []
print(letters3) #['a', 'b', 'C', 'D', 'E', [], 'f', 'g']
print(letters3[6]) #f
letters3[:] = []
print(letters3) #[]

l = []
l.append('AAA')
l.append('BBB')
l.append('CCC')
print(l) #['AAA', 'BBB', 'CCC']
