x = {'apple', 'orange','grape'}
print('orange' in x) #True

s = {1,2,3,2,4}
print(s) #{1, 2, 3, 4}

vec = [[1,2,3],[4,5,6],[7,8,9]]

v = [num for elem in vec for num in elem]
nums = []
for elem in vec:
    for num in elem:
        nums.append(num)
print(nums)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

print(v) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

list = [-10,1,3,20,30]
list.insert(2,5)
print(list) #[-10, 1, 5, 3, 20, 30]
list.append(50)
print(list) #[-10, 1, 5, 3, 20, 30, 50]

#list.sort(reverse= True)
list.reverse()
#list.sort(reverse = False)
print(list) #[50, 30, 20, 5, 3, 1, -10]

print()

names = [(1, 'del'),(2, 'can'), (3, 'angle'),(4, 'bed')]
names.sort(key = lambda name:name[1])
print(names)
#[(3, 'angle'), (4, 'bed'), (2, 'can'), (1, 'del')]
#abc順

import math
print('円周率の値は、{0:.4f}.'.format(math.pi)) #円周率の値は、3.1416.
print('円周率の値は、{0:.5f}.'.format(math.pi)) #円周率の値は、3.14159.

print(filter(lambda n: n % 3 == 0, range(10))) #<filter object at 0x7f8503bd5b80>

