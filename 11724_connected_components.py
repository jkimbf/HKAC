from sys import stdin
lines = stdin.read().splitlines()
N, M = map(int, lines[0].split())
checker = [[False]*N for _ in range(N)]

for line in lines[1:]:
    x, y = map(int, line.split())
    checker[x-1][y-1] = True

print(checker)