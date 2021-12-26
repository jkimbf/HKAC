from collections import deque
from sys import stdin

lines = stdin.read().splitlines()
d = deque()
for line in lines[1:]:
    line = line.split()
    if line[0] == 'push_front':
        d.appendleft(line[1])
    elif line[0] == 'push_back':
        d.append(line[1])
    elif line[0] == 'pop_front':
        print(d.popleft()) if d else print(-1)
    elif line[0] == 'pop_back':
        print(d.pop()) if d else print(-1)
    elif line[0] == 'size':
        print(len(d))
    elif line[0] == 'empty':
        print(1) if not d else print(0)
    elif line[0] == 'front' or line[0] == 'back':
        if d:
            temp = d.popleft() if line[0] == 'front' else d.pop()
            print(temp)
            d.appendleft(temp) if line[0] == 'front' else d.append(temp)
        else:
            print(-1)