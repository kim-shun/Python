
'''
class MyClass:
    ''' ここはなんちゃらです '''
    i = 12345
    
    def __init__(self):
        self.data = []

    def f(self):
        return 'hello world'

x = MyClass()
print(x,'aaa') #<__main__.MyClass object at 0x7fc2c4be0b80> aaa


class MyClass:
    '''A sample example class '''
    i = 12345 #クラス変数

    def f(self):
        return 'hello world'

print(MyClass.i) #12345
print(MyClass.f) #<function MyClass.f at 0x7f8f283d0310>
print(MyClass.__doc__) # A sample example class 
#print(MyClass.f()) #TypeError: f() missing 1 required positional argument: 'self'

obj = MyClass()
print(obj.f) #<bound method MyClass.f of <__main__.MyClass object at 0x7fb4c83d6910>>
print(obj.f()) #hello world
'''
