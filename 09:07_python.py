'''
s = {'A':'apple', 'B':'banana','C':'cherry'}
print(s)

for key in s:
    print(key) #A B C
print()

for value in s:
    print(value) #A B C
print()

for value in s.values():
    print(value) #apple banana cherry
print()

for i in s.values():
    print(i) #apple banana cherry
print()

for items in s.items():
    print(items) #('A', 'apple') ('B', 'banana') ('C', 'cherry')
print()


print(s["A"]) #apple
#print(s["apple"]) #エラー
'''

for i in range(5):
    print(i,"組") #0 1 2 3 4
    for j in range(3):
        print(j, "番") #012 012 012 012 012
    print()

        
print()
