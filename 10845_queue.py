from collections import deque
from sys import stdin

lines = stdin.read().splitlines()
queue = deque()
for line in lines[1:]:
    line = line.split()
    if line[0] == 'push':
        queue.append(line[1])
    elif line[0] == 'pop':
        print(queue.popleft()) if queue else print(-1)
    elif line[0] == 'size':
        print(len(queue))
    elif line[0] == 'empty':
        print(1) if not queue else print(0)
    elif line[0] == 'front' or line[0] == 'back':
        if queue:
            temp = queue.popleft() if line[0] == 'front' else queue.pop()
            print(temp)
            queue.appendleft(temp) if line[0] == 'front' else queue.append(temp)
        else:
            print(-1)