import sys

import time
time.sleep(2)

input = sys.stdin.readline
N, M = map(int, input().split())
set_n, set_m = set(), set()

for n, s in zip([N, M], [set_n, set_m]):
    for _ in range(n):
        s.add(input().rstrip())

res = set_n & set_m
print(*[len(res)]+sorted(res), sep="\n")