from collections import deque

N, K = map(int, input().split())
queue = deque()
queue.extend(range(1, N+1))
out = []

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())
    out.append(queue.popleft())

print('<', end='')
print(*out, sep=', ', end='')
print('>')