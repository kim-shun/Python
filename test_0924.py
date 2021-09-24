#グローバル変数(関数の外部)
#シンボル表
d = "mm\nkoko\\"
print(d)
print(len(d)) #8
#extend

diver = [d * 2 for d in 'diver']

print(diver)
#['dd', 'ii', 'vv', 'ee', 'rr']

l = list(range(3))
print(l)
l.append(l) #[0, 1, 2, [...]]
print(l) #[0, 1, 2, [...]]
del l[3]
print(l)
l.append(100)
print(l)
l.append('new')
print(l)
#[0, 1, 2, 100, 'new']
l.extend([101,102,103])
print(l)
#[0, 1, 2, 100, 'new', 101, 102, 103]
l.extend((-1,-2,-3))
l.extend('new')
print(l)
#[0, 1, 2, 100, 'new', 101, 102, 103, -1, -2, -3, 'n', 'e', 'w']
l.append([11,12,13])
l.append((21,22,23))
print(l)
'''
[0, 1, 2, 100, 'new', 101, 102, 103,
-1, -2, -3, 'n', 'e', 'w',
[11, 12, 13], (21, 22, 23)]
'''

