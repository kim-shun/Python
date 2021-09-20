i = 1
i = 2

def f(arg):
    i = 3
    print(arg)

i = 4
i = 5

f(i) #5
s = set([1,2,3,4,5])                                # set([1,2,3,4,5]) 
s2 = set([1,1,2,2,3,3])                              # set([1,2,3])
s3 = set({'dog':'inu', 'cat':'neko', 'bird':'tori'}) # set(['dog', 'cat', 'bird']) 
print(s)
print(s2)
print(s3)

a = {}
b = set()

a['apple'] = 2
b.update('7')

print(a)  # {'apple': 2}
print(b)  # {'7'}

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
power = list(zip(*matrix))
print(power) #[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
power2 = list(zip(matrix))
print(power2) #[([1, 2, 3],), ([4, 5, 6],), ([7, 8, 9],)]

a2 = [1,3,4,6,3,5]
a2.insert(3, -1)
a2.pop(4)
a2.remove(3)
print(a2) #[1, 4, -1, 3, 5]
a2.remove(3)
print(a2) #[1, 4, -1, 5]
a2.pop(3)
print(a2) #[1, 4, -1]
