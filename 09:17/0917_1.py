class kusanagi():

    def s(self):

        print("Need Speed?")#　 …★a　

        self.m()

    def m(self):#…★b

        print("I'm Saya.")

class wexal(kusanagi):

    def m(self):

        print("I'm David.")

k = kusanagi()

w = wexal()

k.s()

w.s()

#【A】self.m()　【B】m(self):　【C】s()



