#クラス

class User:
    count = 0 #クラス変数
    def __init__(self,name,age):
        User.count += 1
        self.name = name #インスタンス変数
        self.age = age
    #pass
print(User.count) #0
tom = User('Tom',15)
print(tom) #<__main__.User object at 0x7fd0e8efebb0>
print(tom.name) #Tom
bob = User('Bob',16)
print(bob.age) #16
print(User.count) #2
'''
tom = User() #インスタンス
tom.name = 'Tom'
tom.age = 18

bob = User()
intro = bob.introduce = "初めまして"

print(tom.name) #Tom
print(tom.age) #18
print(intro) #初めまして
'''
