from sys import stdin
input = stdin.readline

import time
time.sleep(2)

N, M = map(int, input().split())
nums = []

for _ in range(N):
    nums.append(list(map(int, input().split())))

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    temp = [t[y1-1: y2] for t in nums[x1-1: x2]]
    print(sum([sum(t) for t in temp]))
