from sys import stdin
org_nums = list(map(int, stdin.read().splitlines()[1].split()))
nums = {x: i for i, x in enumerate(sorted(set(org_nums)))}
print(*[nums[x] for x in org_nums], sep=' ')