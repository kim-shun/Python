from collections import deque
queue = deque(["bear", "cow", "dog", "elephant","fox"])
queue.append("goat")
queue.popleft()
print(queue) #deque(['cow', 'dog', 'elephant', 'fox', 'goat'])
queue.pop()
print(queue) #deque(['cow', 'dog', 'elephant', 'fox'])
queue.popright()
print(queue)
