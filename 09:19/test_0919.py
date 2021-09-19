'''
#Pythonのヒストリ情報はユーザーディレクトリの「.python_history」に保存されている。

print((1, 2) > (1, 2, -1)) #False
print((1, 2) > (1, 2, 5)) #False
print((1, 2) > (1, 2, -3,-4)) #False
print((1, 2, 5) > (1, 2, -3,-4)) #True
print(('bb', 'c') > ('bcd', 'a')) #False
print(1 > -1 == (1-2)) #True

c = 'C:\some\name'
rc = r'C:\some\name'
print(rc) #C:\some\name
print(c)
#C:\some
#ame
print(len(rc)) #12
print(len(c)) #11

print()
print()

pairs = [(3,'b'),(1,'c'),(2,'a')]
pairs.sort(key=lambda arg:arg[1])
print(pairs)
#[(2, 'a'), (3, 'b'), (1, 'c')]
'''

loc = "1"

def scope():
    loc = "2"

    def do_local():
        loc = "3"

    def do_nonlocal():
        nonlocal loc
        loc = "4"

    def do_global():
        global loc
        loc = "5"

    do_local()
    print("A:2",loc)
    do_nonlocal()
    print("B:4",loc)
    do_global()
    print("C:4",loc)

print("D:1",loc)

scope()
print("E:5",loc)
    

print()

def scope2():
    loc2 = "init"
    
    def do_local2():
        loc2 = "local"
        
    def do_nonlocal2():
        nonlocal loc2
        loc2 = "nonlocal"

    def do_global2():
        global loc2
        loc2 = "global"

    do_local2()
    print("1:init",loc2)
    do_nonlocal2()
    print("2:nonlocal",loc2)
    do_global2()
    print("3:nonlocal",loc2)

scope2()
print("4:global",loc2)

