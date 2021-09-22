loc = "XXX"
def scope():
    loc = "init"
    print("A",loc)

    def do_local():
        loc = "local"
        print("通過do_local",loc)

    def do_global():
        global loc
        loc = "global"
        print("通過do_global", loc)
    do_local()
    print("B",loc)
    do_global()
    print("C",loc)

print("scope通過前")
print("D", loc)
scope()
print("scope通過後")
print("E", loc)

print()

loc = "XXX"
def scope():
    loc = "init"
    print("A",loc)

    def do_nonlocal():
        nonlocal loc
        loc = "nonlocal"
        print("通過do_nonlocal",loc)

    def do_global():
        global loc
        loc = "global"
        print("通過do_global", loc)
    do_nonlocal()
    print("B",loc)
    do_global()
    print("C",loc)

print("scope通過前")
print("D", loc)
scope()
print("scope通過後")
print("E", loc)

#入れ子構造になると関数内ではglobalが機能しない
#入れ子構造になると、中でも外でもではなく外だけになる
'''
scope通過前
D XXX
A init
通過do_local local
B init
通過do_global global
C init
scope通過後
E global

scope通過前
D XXX
A init
通過do_nonlocal nonlocal
B nonlocal
通過do_global global
C nonlocal
scope通過後
E global
'''

