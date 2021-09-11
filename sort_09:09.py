T = [3,8,6,1,2,5,5,10,9,7]

for i in range(len(T) - 1):
    for j in range(i + 1, len(T)):
        if T[i] > T[j]:
            T[i], T[j] = T[j], T[i]

print(T)
