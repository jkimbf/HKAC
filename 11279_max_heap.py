from sys import stdin
from heapq import heapify, heappush, heappop

nums = []
heapify(nums)

for num in map(int, stdin.read().splitlines()[1:]):
    heappush(nums, -num) if num != 0 else print(-heappop(nums) if nums else 0)

