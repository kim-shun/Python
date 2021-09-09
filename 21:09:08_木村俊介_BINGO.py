import random

b = random.sample(range(1,16),5)
i = random.sample(range(16,31),5)
n = random.sample(range(31,46),5)
g = random.sample(range(46,61),5)
o = random.sample(range(61,76),5)

print("  B |  I |  N |  G |  O ")
for j in range(5):
    print("%3d"  % b[j],end=" |")
    print("%3d"  % i[j],end=" |")
    if j == 2:
        print("   ",end=" |")
    else:
        print("%3d"  % n[j],end=" |")
    print("%3d"  % g[j],end=" |")
    print("%3d"  % o[j])
