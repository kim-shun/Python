#lambdaの使い方
'''
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
'''
squares = list(map(lambda x: x**2, range(10)))
print(squares)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print([x**2 for x in range(10)])
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
