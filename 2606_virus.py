from sys import stdin
lines = stdin.read().splitlines()
N = int(lines[0])
dfs = [[False]*N for _ in range(N)]

for i in range(2, int(lines[1])+2):
    x, y = [int(x) for x in lines[i].split()]
    dfs[x-1][y-1] = True
    dfs[y-1][x-1] = True

output = [False] * N
def search(i):
    output[i] = True
    for ind, val in enumerate(dfs[i]):
        if val and not output[ind]:
            search(ind)

search(0)
print(sum(output[1:]))