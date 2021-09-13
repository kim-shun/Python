#関数の定義


#四角形、三角形の面積を出す


def k3kaku(bottom,height):
    tri = bottom * height / 2
    return tri

def k4kaku(bottom,height):
    sq = bottom * height
    return sq

bottom = int(input("底辺を入力してください："))
height = int(input("高さを入力してください："))

obj1 = k3kaku(bottom,height)
obj2 = k4kaku(bottom,height)

print("三角形の面積は",obj1,"です")
print("四角形の面積は",obj2,"です")


'''
def abc(e,y=5): #yが入ってこなかったら5で計算
    x = e * 3 + y
    return x
#obj = abc(3)
obj = abc(3,1)
print(obj)

def ask2(a, b = 4, c = 'Please try again!'): #デフォルト値
    x = a * b
    print(x,c)

ask2(3,3) #9 Please try again!
ask2(3,c="test") #12 test
ask2(3,c="test", b = 8) #24 test
'''
