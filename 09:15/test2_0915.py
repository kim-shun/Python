'''
from collections import deque
queue = deque(["bear", "cow", "dog", "elephant","fox"])
queue.append("goat")
queue.popleft()
print(queue) #deque(['cow', 'dog', 'elephant', 'fox', 'goat'])
queue.pop()
print(queue) #deque(['cow', 'dog', 'elephant', 'fox'])
'''
q = ["bear", "cow", "dog", "elephant","fox"]
#q.popleft() #AttributeError: 'list' object has no attribute 'popleft'
q.pop() #['bear', 'cow', 'dog', 'elephant']
print(q)

print([(x,y) for x in [1,2,3] for y in [3,1,2] if x != y])
#[(1, 3), (1, 2), (2, 3), (2, 1), (3, 1), (3, 2)]
combs = []
for x in [1,2,3]:
    for y in [3,1,2]:
        if x != y:
            combs.append((x,y))
print(combs) #[(1, 3), (1, 2), (2, 3), (2, 1), (3, 1), (3, 2)]
