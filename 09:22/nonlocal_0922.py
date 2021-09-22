loc0 = "XXX"
def scope0():
    loc0 = "init"
    print("A",loc0)

    def do_local0():
        loc0 = "local"
        print("通過do_local",loc0)

    do_local0()
    print("B",loc0)

print("C", loc0)
print("scope呼び出し前")
scope0()
print("scope呼び出し後")
print("D",loc0)


print()

loc = "XXX"
def scope():
    loc = "init"
    print("A",loc)

    def do_nonlocal():
        nonlocal loc
        loc = "nonlocal"
        print("通過nonlocal",loc)

    do_nonlocal()
    print("B",loc)
print("C", loc)
print("scope呼び出し前")
scope()
print("scope呼び出し後")
print("D",loc)

print()

loc2 = "XXX"
def scope2():
    loc2 = "init"
    print("A",loc2)


print("B",loc2)
scope2()
print("C",loc2)
