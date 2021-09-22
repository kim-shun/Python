
def scope():
    loc = "init"
    print("A",loc)

    def do_local():
        loc = "local"
        print("B",loc)

    def do_nonlocal():
        nonlocal loc
        loc = "nonlocal"

    def do_global():
        global loc
        loc = "global"

    do_local()
    print("C",loc)
    do_nonlocal()
    print("D", loc)
    do_global()
    print("E",loc)

scope()
print("F",loc)
