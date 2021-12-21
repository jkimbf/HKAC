from itertools import combinations
N, M = map(int, input().split())
nums = list(map(int, input().split()))
comb = [sum(x) for x in list(combinations(nums, 3))]
print(max(filter((M).__ge__, comb)))
