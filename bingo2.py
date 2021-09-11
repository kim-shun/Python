import random

bingo = [random.sample(range(n,n + 15), 5) for n in range(1, 76, 15) ]
bingo[2][2] = ""

print("  B |  I |  N |  G |  O ")
for row in zip(*bingo):
    print(*map("{:>3}".format, row), sep=" |")
