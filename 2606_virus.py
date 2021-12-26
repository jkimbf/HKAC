from sys import stdin
lines = stdin.read().splitlines()
N = int(lines[0])
dfs = [[0 for _ in range(N)] for _ in range(N)]

for i in range(2, int(lines[1])+2):
    x, y = [int(x) for x in lines[i].split()]
    dfs[x-1][y-1] += 1
    dfs[y-1][x-1] += 1

output = list(range(N))

import numpy as np
print(np.array(dfs))