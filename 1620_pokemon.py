from sys import stdin
input = stdin.readline

import time
time.sleep(2)

N, M = map(int, input().split())
dokam = {}

for i in range(N):
    n = input().strip()
    dokam[n] = i+1
    dokam[i+1] = n

for _ in range(M):
    cmd = input().strip()
    print(dokam[int(cmd)]) if cmd.isdigit() else print(dokam[cmd])
