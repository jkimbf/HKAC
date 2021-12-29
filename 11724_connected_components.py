from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)

lines = stdin.read().splitlines()
N, M = map(int, lines[0].split())
g = [[False]*N for _ in range(N)]
v = [False]*N

def check(g, v, x):
    if v[x-1]:
        return

    v[x-1] = True 
    for i, ind in enumerate(g[x-1]):
        if ind and not v[i]:
            check(g, v, i+1)

for line in lines[1:]:
    x, y = map(int, line.split())
    g[x-1][y-1] = True
    g[y-1][x-1] = True

count = 0
for x in range(1, N+1):
    if not v[x-1]:
        check(g, v, x)
        count += 1

print(count)