from collections import deque

for _ in range(int(input())):
    line = input()
    stack = deque()
    YES = True
    for c in line:
        if c == '(':
            stack.append(c)
        elif not stack:
            YES = False
            break
        else:
            stack.pop()
    print('YES') if YES and not stack else print('NO')