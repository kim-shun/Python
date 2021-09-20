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
    print("A:",loc) #【A】
    do_nonlocal()
    print("B:",loc) #【B】
    do_global()
    print("C:",loc) #【C】

print("D:",loc) #【D】
scope()
print("E:",loc) #【E】
    

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
    print("F:",loc2) #【F】
    do_nonlocal2()
    print("G:",loc2) #【G】
    do_global2()
    print("H:",loc2) #【H】

scope2()
print("I:",loc2) #【I】

