import time
time.sleep(3)

import sys
sys.setrecursionlimit(1000000)


def check(mat, checked, M, N, x, y):
    checked[y][x] = True

    if (y+1 < N) and (mat[y+1][x] == 1) and (not checked[y+1][x]):
        check(mat, checked, M, N, x, y+1)
    if (x+1 < M) and (mat[y][x+1] == 1) and (not checked[y][x+1]):
        check(mat, checked, M, N, x+1, y)
    if (y-1 >= 0) and (mat[y-1][x] == 1) and (not checked[y-1][x]):
        check(mat, checked, M, N, x, y-1)
    if (x-1 >= 0) and (mat[y][x-1] == 1) and (not checked[y][x-1]):
        check(mat, checked, M, N, x-1, y)


for _ in range(int(input())):
    M, N, K = map(int, input().split())

    mat = [[0]*M for _ in range(N)]
    checked = [[False]*M for _ in range(N)]

    coords = []
    for _ in range(K):
        x, y = map(int, input().split())
        coords.append((x,y))
        mat[y][x] = 1

    counter = 0
    for x, y in coords:
        if not checked[y][x]:
            check(mat, checked, M, N, x, y)
            counter += 1
    print(counter)