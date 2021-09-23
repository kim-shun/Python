
def scope():
    loc = "init"
    print("A",loc)

    def do_local():
        loc = "local"

    def do_nonlocal():
        nonlocal loc
        loc = "nonlocal"

    def do_global():
        global loc
        loc = "global"

    do_local()
    print("B",loc)
    do_nonlocal()
    print("C", loc)
    do_global()
    print("D",loc)

scope()
print("E",loc)
