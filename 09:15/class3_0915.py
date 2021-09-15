'''
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i) #3.0 -4.5

class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Tama')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks) #['roll over', 'play dead']

'''

