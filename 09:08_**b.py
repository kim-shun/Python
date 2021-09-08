'''
def f(a, *b, **c):
    print("必須引数 ->", a) #test
    print("仮引数タプル ->", b) #(3, 7, 8)
    print("仮引数辞書 ->", c) #{'dic': 'bob', 'dic2': 'Jon'}

    for arg in b:
        print(arg)
        
    print('-' * 40)
    
    for kw in c:
        print(kw,':', c[kw])

f('test',3,7,8,dic='bob',dic2='Jon')
#*bの後に*cを書かなければいけない
f('Value_to_enter_A','tuple_1個目','tuple_2個目',dic1='Bob',dic2='Jon',dic5='Arisa')


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)

    print("-" * 40)

    for kw in keywords:
         print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
'''

def price(kid, adult):
    amount = kid * 500 + adult * 1000
    print(amount)


price(2,3)
price(5,2)

print('-' * 40)

def f(a, L=[]):
    L.append(a ** 4)
    print(L)


f(1)
f(7)
f(3)


