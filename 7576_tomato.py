from sys import stdin
from collections import deque

lines = stdin.read().splitlines()
M, N = map(int, lines[0].split())
nums = [list(map(int, l.split())) for l in lines[1:]]
visited = [[False]*M for _ in range(N)]

if all([all(v) for v in visited]):
    print(0)

queue = deque()
for n in range(N):
    for m in range(M):
        if nums[n][m] != 0:
            visited[n][m] = True
            if nums[n][m] == 1:
                queue.append((n, m, 0))

found = False
while queue:
    n, m, count = queue.popleft()

    if not n+1 >= N and not visited[n+1][m] and nums[n+1][m] == 0:
        visited[n+1][m] = True
        queue.append((n+1, m, count+1))
    if not m+1 >= M and not visited[n][m+1] and nums[n][m+1] == 0:
        visited[n][m+1] = True
        queue.append((n, m+1, count+1))
    if not n-1 < 0 and not visited[n-1][m] and nums[n-1][m] == 0:
        visited[n-1][m] = True
        queue.append((n-1, m, count+1))
    if not m-1 < 0 and not visited[n][m-1] and nums[n][m-1] == 0:
        visited[n][m-1] = True
        queue.append((n, m-1, count+1))

print(count) if all([all(v) for v in visited]) else print(-1)