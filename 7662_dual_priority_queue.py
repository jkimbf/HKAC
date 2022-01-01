from sys import stdin
from heapq import heapify, heappush, heappop
import time
time.sleep(3)


for _ in range(int(input())):
    max_h = []
    min_h = []
    heapify(max_h)
    heapify(min_h)
    for _ in range(int(input())):
        print(max_h)
        print(min_h)
        cmd, num = input().split()
        num = int(num)
        if cmd == 'I':
            heappush(min_h, num)
            heappush(max_h, -num)
        else:
            if min_h:
                heappop(max_h)
                heappop(min_h)

    if min_h and max_h:
        print(heappop(max_h), heappop(min_h))
    else:
        print('EMPTY')