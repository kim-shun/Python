def f(a, L=[]):
    L.append(a ** 4)
    return L

#obj = f(4,[5])
#print(obj)
print(f(1)) #[1]
print(f(7)) #[1, 2401]
print(f(3)) #[1, 2401, 81]
#rubyとは違って呼び出される都度増える

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f2(1)) #[1]
print(f2(7)) #[7]
print(f2(3)) #[3]

#その都度初期化される

print(f2(4,L=[5])) #[5,4]
