from collections import deque
from sys import stdin

lines = stdin.read().splitlines()
stack = deque()
for line in lines[1:]:
    line = line.split()
    if line[0] == 'push':
        stack.append(line[1])
    elif line[0] == 'pop':
        print(stack.pop()) if stack else print(-1)
    elif line[0] == 'size':
        print(len(stack))
    elif line[0] == 'empty':
        print(1) if not stack else print(0)
    elif line[0] == 'top':
        if stack:
            top = stack.pop()
            print(top)
            stack.append(top)
        else:
            print(-1)