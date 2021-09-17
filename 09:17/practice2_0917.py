
def scope():
    loc = "init"
    
    def do_local():
        loc = "local"
        
    def do_nonlocal():
        nonlocal loc
        loc = "nonlocal"

    def do_global():
        global loc
        loc = "global"

    do_local()
    print(loc) #A
    do_nonlocal()
    print(loc) #B
    do_global()
    print(loc) #C

scope()
print(loc) #D

print()
'''

#Need Speed?
#I'm Saya.
#Need Speed?
#I'm David.


class kusanagi():

    def s(self):
        print("Need Speed?")
        self.m()

    def m(self):
        print("I'm Saya.")

class wexal(kusanagi):
    def m(self):
        print("I'm David.")

k = kusanagi()
w = wexal()
k.s()
w.s()
'''

#Magatama is a
#Saya's
#reliable
#partner


class kusanagi(Exception):
    pass

def raise_character(a):
    print("【A】")
    raise kusanagi
    print("【B】")

def func(name: int):
    try:
        print(name, "【C】")
        raise_character(name)
    except kusanagi:
        print("【D】")
        raise Exception

name = "Magatama"
try:
    func(name)
except Exception:
    print("【E】")

#Magatama is a
#Saya's
#reliable
#partner
